import os
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import io
import pyttsx3

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate


HF_TOKEN = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
if HF_TOKEN:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

HF_REPO_ID = os.environ.get("HF_REPO_ID", "HuggingFaceH4/zephyr-7b-beta")
DB_FAISS_PATH = "vectorstore/db_faiss"

CUSTOM_PROMPT_TEMPLATE = """
You are Dr. Ava, a compassionate and knowledgeable AI medical assistant. You help patients understand medical information based on the provided context. 

IMPORTANT GUIDELINES:
- Always be empathetic and professional in your responses
- Use the medical information from the context to answer questions
- If you don't know the answer, say so clearly and suggest consulting a healthcare professional
- Never provide specific medical diagnoses or treatment recommendations
- Always remind patients that you are an AI assistant and they should consult healthcare professionals for medical decisions
- Be encouraging and supportive while maintaining medical accuracy

Context: {context}
Question: {question}

Provide a helpful, empathetic response based on the context above.
"""


def build_qa_chain():
    if not HF_TOKEN:
        raise RuntimeError("Missing HF token. Set HF_TOKEN or HUGGINGFACEHUB_API_TOKEN.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

    endpoint = HuggingFaceEndpoint(
        repo_id=HF_REPO_ID,
        task="conversational",
        temperature=0.5,
        max_new_tokens=512,
        top_p=0.9,
        huggingfacehub_api_token=HF_TOKEN,
    )
    chat_llm = ChatHuggingFace(llm=endpoint)

    prompt = PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"])

    qa = RetrievalQA.from_chain_type(
        llm=chat_llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )
    return qa


qa_chain = build_qa_chain()

app = FastAPI(title="Medical Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.post("/api/ask")
async def ask(request: Request):
    body = await request.json()
    question = (body.get("question") or "").strip()
    if not question:
        return JSONResponse(status_code=400, content={"error": "question is required"})

    result = qa_chain.invoke({"query": question})

    return {
        "answer": result.get("result", ""),
    }


@app.post("/api/speak")
async def speak(request: Request):
    """Convert text to speech for the AI avatar"""
    body = await request.json()
    text = body.get("text", "").strip()
    if not text:
        return JSONResponse(status_code=400, content={"error": "text is required"})
    
    try:
        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        
        # Set voice properties for a more natural female voice (Zira)
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'zira' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        
        # Set speech rate and volume for natural conversation
        engine.setProperty('rate', 160)  # Slightly faster for better engagement
        engine.setProperty('volume', 0.9)  # Higher volume for clarity
        
        # Create temporary file for audio output
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        # Generate speech to temporary file
        engine.save_to_file(text, temp_path)
        engine.runAndWait()
        
        # Read the generated audio file
        with open(temp_path, 'rb') as audio_file:
            audio_data = audio_file.read()
        
        # Clean up temporary file
        os.unlink(temp_path)
        
        # Return audio data
        return StreamingResponse(
            io.BytesIO(audio_data),
            media_type="audio/wav",
            headers={
                "Content-Disposition": "attachment; filename=dr_ava_response.wav",
                "Cache-Control": "no-cache"
            }
        )
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"TTS failed: {str(e)}"})


@app.get("/api/tts-test")
async def tts_test():
    """Test endpoint to verify TTS functionality"""
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        voice_info = []
        for voice in voices:
            voice_info.append({
                "name": voice.name,
                "id": voice.id,
                "is_female": 'zira' in voice.name.lower() or 'female' in voice.name.lower()
            })
        
        return {
            "status": "TTS is working",
            "available_voices": voice_info,
            "current_voice": "Microsoft Zira Desktop (Female voice selected)",
            "speech_rate": 160,
            "volume": 0.9
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"TTS test failed: {str(e)}"})


if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment variable (for Vercel deployment)
    port = int(os.environ.get("PORT", 8000))
    
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=False)




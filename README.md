# 🏥 Dr. Ava - AI Medical Assistant with 3D Avatar

Dr. Ava is an advanced medical chatbot featuring a 3D AI avatar that provides empathetic medical information assistance. The avatar can speak responses, animate during conversations, and offers a more engaging user experience.

![Dr. Ava Medical Assistant](https://img.shields.io/badge/Dr.%20Ava-Medical%20Assistant-blue?style=for-the-badge&logo=medical&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.117+-green?style=for-the-badge&logo=fastapi&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-black?style=for-the-badge&logo=vercel&logoColor=white)

## ✨ Features

### 🤖 3D AI Avatar
- **Interactive 3D Character**: A friendly medical assistant avatar with facial features and medical accessories
- **Real-time Animations**: Breathing, gentle movements, and speaking animations
- **Status Indicators**: Visual feedback showing avatar state (thinking, speaking, ready)
- **Responsive Design**: Avatar adapts to different screen sizes

### 🔊 Text-to-Speech
- **Natural Voice**: AI responses are converted to speech using pyttsx3
- **Auto-speak**: Responses are automatically spoken (can be disabled)
- **Manual Controls**: Speak button to replay responses, mute/unmute functionality
- **Voice Customization**: Female voice with optimized speech rate and volume

### 👩‍⚕️ Enhanced Medical Persona
- **Dr. Ava Identity**: The AI presents itself as a compassionate medical assistant
- **Professional Guidelines**: Empathetic responses with proper medical disclaimers
- **Safety First**: Always reminds users to consult healthcare professionals
- **Contextual Awareness**: Uses medical encyclopedia knowledge effectively

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dr-ava-medical-chatbot.git
   cd dr-ava-medical-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   export HF_TOKEN=your_huggingface_token_here
   export HF_REPO_ID=HuggingFaceH4/zephyr-7b-beta
   ```

4. **Run the application**
   ```bash
   python server.py
   ```

5. **Access the interface**
   Open your browser and go to `http://localhost:8000`

### 🎮 Avatar Controls

#### Visual Interface
- **Avatar Display**: 3D character in the left panel
- **Status Badge**: Shows current state (Ready, Thinking, Speaking, etc.)
- **Speak Button**: Replay the last AI response
- **Mute Button**: Toggle audio on/off

#### Interactions
- **Auto-animation**: Avatar breathes and moves naturally
- **Speaking Animation**: Special movements when the avatar is speaking
- **Status Updates**: Real-time feedback on avatar actions

## 🔧 Technical Features

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: Framework for developing LLM-powered applications
- **Hugging Face**: Integration with Hugging Face models
- **FAISS**: Efficient similarity search and clustering
- **pyttsx3**: Cross-platform text-to-speech library

### Frontend
- **Three.js**: 3D graphics and animations
- **Tailwind CSS**: Utility-first CSS framework
- **Responsive Design**: Works on desktop and mobile devices
- **Web Audio API**: Audio playback and management

## 🚀 Deployment

### Vercel Deployment

1. **Fork this repository** to your GitHub account

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with your GitHub account
   - Click "New Project"
   - Import your forked repository

3. **Set Environment Variables**
   - In Vercel dashboard, go to Settings → Environment Variables
   - Add the following variables:
     - `HF_TOKEN`: Your Hugging Face API token
     - `HF_REPO_ID`: `HuggingFaceH4/zephyr-7b-beta` (or your preferred model)

4. **Deploy**
   - Click "Deploy" button
   - Wait for deployment to complete
   - Your app will be available at `https://your-project.vercel.app`

### Manual Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

## 🛠️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `HF_TOKEN` | Hugging Face API token | Required |
| `HF_REPO_ID` | Hugging Face model repository ID | `HuggingFaceH4/zephyr-7b-beta` |
| `PORT` | Server port | `8000` |

### Customization

- **Avatar Appearance**: Modify the Three.js avatar creation in `static/index.html`
- **Voice Settings**: Adjust TTS parameters in `server.py`
- **Medical Knowledge**: Replace PDF files in `data/` directory
- **UI Theme**: Customize colors and styling in `static/index.html`

## 🔒 Safety & Ethics

Dr. Ava includes built-in safety features:
- **Medical Disclaimers**: Always reminds users about AI limitations
- **Professional Boundaries**: No specific diagnoses or treatments
- **Healthcare Guidance**: Encourages consultation with medical professionals
- **Empathetic Responses**: Compassionate and supportive communication

## 📱 Browser Compatibility

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the AI models
- [LangChain](https://langchain.com/) for the LLM framework
- [Three.js](https://threejs.org/) for 3D graphics
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [Vercel](https://vercel.com/) for hosting platform

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Check the documentation
- Review the troubleshooting section

---

**Important**: Dr. Ava is an AI assistant for educational purposes only. Always consult qualified healthcare professionals for medical decisions.

## 🌟 Star this repository if you found it helpful!


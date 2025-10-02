# 🏥 Dr. Ava - AI Medical Assistant with 3D Avatar

Dr. Ava is an advanced medical chatbot featuring a 3D AI avatar that provides empathetic medical information assistance. The avatar can speak responses, animate during conversations, and offers a more engaging user experience.

## ✨ New Features

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

### 1. Install Dependencies
```bash
# Run the installation script
python install_requirements.py

# Or install manually
pip install langchain langchain-community langchain-huggingface faiss-cpu pypdf pyttsx3 fastapi uvicorn
```

### 2. Set Environment Variables
```bash
# Set your Hugging Face token
export HF_TOKEN=your_huggingface_token_here
```

### 3. Run the Application
```bash
python server.py
```

### 4. Access the Interface
Open your browser and go to `http://localhost:8000`

## 🎮 Avatar Controls

### Visual Interface
- **Avatar Display**: 3D character in the left panel
- **Status Badge**: Shows current state (Ready, Thinking, Speaking, etc.)
- **Speak Button**: Replay the last AI response
- **Mute Button**: Toggle audio on/off

### Interactions
- **Auto-animation**: Avatar breathes and moves naturally
- **Speaking Animation**: Special movements when the avatar is speaking
- **Status Updates**: Real-time feedback on avatar actions

## 🔧 Technical Features

### Backend Enhancements
- **Enhanced Prompt**: Medical assistant persona with safety guidelines
- **TTS Endpoint**: `/api/speak` for text-to-speech conversion
- **Voice Optimization**: Female voice with natural speech patterns

### Frontend Features
- **Three.js Integration**: 3D graphics and animations
- **Responsive Layout**: 4-column grid layout with avatar prominence
- **Audio Management**: Web Audio API integration for speech playback
- **State Management**: Avatar state tracking and visual feedback

## 🎨 Avatar Customization

The avatar is built using Three.js and includes:
- **Face**: Spherical head with eyes and mouth
- **Medical Accessories**: Stethoscope for professional appearance
- **Animations**: Breathing, rotation, and speaking movements
- **Materials**: Skin-tone coloring with medical theming

## 🔒 Safety & Ethics

Dr. Ava includes built-in safety features:
- **Medical Disclaimers**: Always reminds users about AI limitations
- **Professional Boundaries**: No specific diagnoses or treatments
- **Healthcare Guidance**: Encourages consultation with medical professionals
- **Empathetic Responses**: Compassionate and supportive communication

## 🛠️ Troubleshooting

### Common Issues

1. **Avatar not displaying**
   - Check browser console for Three.js errors
   - Ensure JavaScript is enabled
   - Try refreshing the page

2. **Text-to-speech not working**
   - Check if pyttsx3 is properly installed
   - Verify audio permissions in browser
   - Try the mute/unmute button

3. **Performance issues**
   - Close other browser tabs
   - Check system resources
   - Try reducing browser zoom level

### System Requirements
- **Python**: 3.8+ recommended
- **Browser**: Modern browser with WebGL support
- **Audio**: Audio output device for text-to-speech
- **Memory**: 4GB+ RAM recommended

## 📱 Browser Compatibility

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

## 🔮 Future Enhancements

Potential improvements for Dr. Ava:
- **Advanced 3D Models**: More detailed character models
- **Facial Expressions**: Emotion-based animations
- **Voice Cloning**: Custom voice synthesis
- **Multi-language**: Support for multiple languages
- **Accessibility**: Enhanced accessibility features

## 📄 License

This project maintains the same license as the original medical chatbot.

---

**Important**: Dr. Ava is an AI assistant for educational purposes only. Always consult qualified healthcare professionals for medical decisions.

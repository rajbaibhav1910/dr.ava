# 🚀 Deployment Guide - Dr. Ava Medical Assistant

This guide will help you deploy Dr. Ava to various platforms including Vercel, GitHub Pages, and other hosting services.

## 📋 Prerequisites

- GitHub account
- Hugging Face account and API token
- Vercel account (for Vercel deployment)

## 🔧 Environment Variables

You'll need to set up these environment variables:

### Required Variables
- `HF_TOKEN`: Your Hugging Face API token
- `HF_REPO_ID`: Model repository ID (default: `HuggingFaceH4/zephyr-7b-beta`)

### How to Get Hugging Face Token
1. Go to [Hugging Face](https://huggingface.co/)
2. Sign up/Login to your account
3. Go to Settings → Access Tokens
4. Create a new token with "Read" permissions
5. Copy the token (starts with `hf_`)

## 🌐 Vercel Deployment (Recommended)

### Step 1: Prepare Repository
1. **Fork this repository** to your GitHub account
2. **Clone locally** (optional, for customization):
   ```bash
   git clone https://github.com/YOUR_USERNAME/dr-ava-medical-chatbot.git
   cd dr-ava-medical-chatbot
   ```

### Step 2: Deploy to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Sign in with your GitHub account
3. Click **"New Project"**
4. Import your forked repository
5. Configure the project:
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)

### Step 3: Set Environment Variables
In the Vercel dashboard:
1. Go to your project → **Settings** → **Environment Variables**
2. Add the following variables:
   ```
   HF_TOKEN = your_huggingface_token_here
   HF_REPO_ID = HuggingFaceH4/zephyr-7b-beta
   ```
3. Click **Save**

### Step 4: Deploy
1. Go to **Deployments** tab
2. Click **"Deploy"** or **"Redeploy"**
3. Wait for deployment to complete
4. Your app will be available at `https://your-project-name.vercel.app`

## 🔄 GitHub Actions (Alternative)

If you prefer GitHub Actions for deployment:

### Step 1: Create GitHub Actions Workflow
Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Vercel

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to Vercel
      uses: amondnet/vercel-action@v20
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.ORG_ID }}
        vercel-project-id: ${{ secrets.PROJECT_ID }}
        working-directory: ./
```

### Step 2: Add Secrets
In your GitHub repository:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add these secrets:
   - `VERCEL_TOKEN`: Your Vercel token
   - `ORG_ID`: Your Vercel organization ID
   - `PROJECT_ID`: Your Vercel project ID

## 🐳 Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "server.py"]
```

### Build and Run
```bash
docker build -t dr-ava .
docker run -p 8000:8000 -e HF_TOKEN=your_token dr-ava
```

## 🌍 Other Hosting Platforms

### Railway
1. Connect your GitHub repository
2. Set environment variables
3. Deploy automatically

### Render
1. Create a new Web Service
2. Connect your repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python server.py`
5. Add environment variables

### Heroku
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set environment variables: `heroku config:set HF_TOKEN=your_token`
4. Deploy: `git push heroku main`

## 🔍 Troubleshooting

### Common Issues

#### 1. Build Failures
- **Issue**: Missing dependencies
- **Solution**: Check `requirements.txt` is complete

#### 2. Environment Variables Not Working
- **Issue**: Variables not set correctly
- **Solution**: Double-check variable names and values

#### 3. TTS Not Working
- **Issue**: pyttsx3 doesn't work on serverless
- **Solution**: TTS is disabled on Vercel (serverless limitation)

#### 4. Large File Size
- **Issue**: Vectorstore files too large
- **Solution**: Consider using external vector database

### Performance Optimization

#### For Production:
1. **Enable Caching**: Add Redis for session management
2. **CDN**: Use Vercel's CDN for static files
3. **Database**: Consider external vector database
4. **Monitoring**: Add logging and monitoring

#### For Development:
1. **Local Testing**: Test with `python server.py`
2. **Environment**: Use `.env` file for local development
3. **Debugging**: Enable debug mode in development

## 📊 Monitoring and Analytics

### Vercel Analytics
1. Enable Vercel Analytics in dashboard
2. Monitor performance and usage
3. Set up alerts for errors

### Custom Monitoring
```python
# Add to server.py
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response
```

## 🔐 Security Considerations

### Production Security:
1. **HTTPS**: Always use HTTPS in production
2. **CORS**: Configure CORS properly
3. **Rate Limiting**: Add rate limiting to prevent abuse
4. **Input Validation**: Validate all inputs
5. **Secrets**: Never commit secrets to repository

### Environment Security:
```bash
# Create .env file (don't commit)
HF_TOKEN=your_token_here
HF_REPO_ID=your_model_here
```

## 📈 Scaling Considerations

### For High Traffic:
1. **Load Balancing**: Use multiple instances
2. **Caching**: Implement Redis caching
3. **Database**: Use external vector database
4. **CDN**: Use global CDN for static files

### Cost Optimization:
1. **Serverless**: Use Vercel's serverless functions
2. **Caching**: Cache responses to reduce API calls
3. **Monitoring**: Monitor usage and costs

## 🆘 Support

If you encounter issues:
1. Check the logs in your hosting platform
2. Verify environment variables are set correctly
3. Test locally first
4. Open an issue on GitHub

---

**Happy Deploying! 🚀**


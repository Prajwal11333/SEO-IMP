# SEO Project - Complete Frontend & Backend Integration

This project integrates multiple SEO tools including Content Generation and Competitor Analysis with React frontend components and Python backend services.

## 🚀 Quick Start

### Option A: Use the Complete Startup Script (Recommended)

Run the startup script to start all services:
```bash
# Windows
start_server_test.bat

# This will start:
# - Content Generator (port 8001)
# - Competitor Analysis (port 8002)  
# - Node.js Proxy (port 3001)
```

### Option B: Manual Setup

#### 1. Backend Services Setup

Navigate to the backend directory:
```bash
cd backend/node-server/python-service
```

**Create virtual environment:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

**Install dependencies:**
```bash
# Install general dependencies
pip install -r requirements.txt

# Install Content Generator dependencies
cd generator
pip install -r requirements.txt

# Install Competitor Analysis dependencies
cd ../Competitor
pip install -r requirements.txt
```

**Start services:**

**Content Generator (port 8001):**
```bash
cd generator
python app.py
```

**Competitor Analysis (port 8002):**
```bash
cd Competitor
python app.py
```

**Node.js Proxy (port 3001):**
```bash
cd ../../node-Server
node Server.js
```

### 2. Frontend Setup

Navigate to the frontend directory:
```bash
cd seoz-frontend
```

Install dependencies and start the development server:
```bash
npm install
npm run dev
```

## 🔧 Configuration

### Service Architecture

The project consists of multiple services:

- **Frontend** (React): `http://localhost:5173`
- **Node.js Proxy**: `http://localhost:3001` (routes requests to backend services)
- **Content Generator**: `http://localhost:8001` (AI content generation)
- **Competitor Analysis**: `http://localhost:8002` (competitor tracking & analysis)

### Backend Configuration

#### Content Generator (port 8001)
- `POST /api/ai-writer/generate-content` - Main content generation endpoint
- `GET /health` - Health check
- `GET /docs` - API documentation

#### Competitor Analysis (port 8002)
- `POST /api/competitor-analysis/analyze` - Start competitor analysis
- `GET /api/competitor-analysis/status/{id}` - Check analysis status
- `GET /api/competitor-analysis/serp` - Get SERP data
- `POST /api/competitor-analysis/predictions` - Get AI predictions
- `POST /api/competitor-analysis/strategy` - Get strategy recommendations
- `GET /health` - Health check
- `GET /docs` - API documentation

#### Node.js Proxy (port 3001)
- Routes all requests to appropriate backend services
- Handles CORS and authentication
- Provides unified API interface
- Real-time updates via Socket.IO

## 📝 API Integration Details

### Content Generation API

The frontend sends requests to `/api/ai-writer/generate-content` with the following structure:

```json
{
  "content_type": "blog",
  "topic": "Digital Marketing Strategies",
  "keywords": ["digital marketing", "SEO", "content strategy"],
  "target_audience": "business",
  "tone": "professional",
  "word_count": 1500,
  "competition_level": "medium"
}
```

### Response Format

The backend returns structured content with SEO scores and predictions:

```json
{
  "content_id": "content_12345",
  "content": {
    "topic": "Digital Marketing Strategies",
    "content_type": "blog",
    "word_count": 1500,
    "full_text": "Generated content...",
    "html": "<h1>Generated content...</h1>",
    "seo_score": {
      "overall": 85,
      "keyword_density": 3.2,
      "readability": 90,
      "meta_tags": 85,
      "heading_structure": 90,
      "content_length": 95
    },
    "metadata": "SEO metadata..."
  },
  "predictions": {
    "ranking_potential": "High",
    "estimated_traffic": "850-1275 visitors/month",
    "competition_level": "Medium",
    "recommended_actions": [...]
  },
  "schedule": {
    "optimal_posting_time": "Tuesday 10:00 AM",
    "frequency": "Weekly",
    "next_post_date": "2024-01-15",
    "content_calendar": [...]
  }
}
```

### Competitor Analysis API

The frontend sends requests to `/api/competitor-analysis/analyze` with the following structure:

```json
{
  "your_domain": "https://example.com",
  "keywords": ["seo tools", "analytics", "marketing"],
  "competitors": ["competitor1.com", "competitor2.com"],
  "depth": 20
}
```

**Response:**
```json
{
  "analysis_id": "ca_20241201_143022",
  "status": "processing",
  "created_at": "2024-12-01T14:30:22"
}
```

**Status Check:**
```http
GET /api/competitor-analysis/status/{analysis_id}
```

**Results:**
```json
{
  "analysis_id": "ca_20241201_143022",
  "status": "completed",
  "progress": 100,
  "results": {
    "your_domain": "https://example.com",
    "keywords": ["seo tools", "analytics"],
    "competitors": ["competitor1.com", "competitor2.com"],
    "summary": {
      "total_keywords": 3,
      "competitors_analyzed": 2,
      "opportunities_found": 5
    },
    "serp_analysis": {...},
    "competitor_analysis": {...},
    "predictions": {...},
    "strategies": {...}
  }
}
```

## 🎯 Features

### Content Generation Features
- **Blog Post**: 800-2000 words, SEO-optimized
- **Landing Page**: 300-600 words, conversion-focused
- **App Description**: 150-300 words, engaging
- **Product Page**: 400-800 words, descriptive

### Competitor Analysis Features
- **SERP Scraping**: Real-time search results analysis
- **Competitor Detection**: Automatic competitor identification
- **Ranking Analysis**: Position tracking across keywords
- **AI Predictions**: Future ranking forecasts
- **Strategy Recommendations**: Actionable SEO strategies
- **Gap Analysis**: Content and keyword opportunities
- **Analysis Depth Options**:
  - Quick (5 results): ~2 minutes
  - Standard (10 results): ~5 minutes
  - Deep (20 results): ~10 minutes

### SEO Features
- Keyword optimization
- SEO score calculation
- Ranking predictions
- Content scheduling
- Meta tag generation
- Real-time competitor monitoring

## 🔍 Testing the Integration

### Test Content Generation
1. Start all backend services
2. Start the frontend development server
3. Navigate to the ContentAI component
4. Fill out the form with:
   - Content type: Blog Post
   - Topic: "Digital Marketing Strategies"
   - Keywords: "digital marketing, SEO, content strategy"
   - Target audience: Business Professionals
   - Tone: Professional
5. Click "Generate SEO Content"
6. Wait for the AI to generate content (10-30 seconds)
7. Review the generated content, SEO scores, and predictions

### Test Competitor Analysis
1. Navigate to the CompetitorAnalysis component
2. Fill out the form with:
   - Your Domain: "https://example.com"
   - Keywords: "seo tools, analytics, marketing"
   - Known Competitors: "competitor1.com, competitor2.com" (optional)
   - Analysis Depth: Deep (20 results)
3. Click "Start Analysis"
4. Monitor real-time progress updates
5. Wait for analysis completion (2-10 minutes depending on depth)
6. Review competitor insights, predictions, and strategy recommendations

### Test Integration Script
Run the automated test script:
```bash
python test_competitor_integration.py
```

## 🛠️ Troubleshooting

### Common Issues

1. **CORS Errors**: Make sure all backend services are running on correct ports
2. **API Key Issues**: Ensure your OpenAI API key is set in the .env file
3. **Connection Refused**: Check that all services are running:
   - Content Generator: http://localhost:8001/health
   - Competitor Analysis: http://localhost:8002/health
   - Node.js Proxy: http://localhost:3001/health
4. **Content Not Generating**: Check the browser console for error messages
5. **Analysis Not Starting**: Verify competitor analysis service is running
6. **Port Conflicts**: Make sure ports 3001, 8001, and 8002 are available

### Service Health Checks

Check individual service health:
```bash
# Content Generator
curl http://localhost:8001/health

# Competitor Analysis
curl http://localhost:8002/health

# Node.js Proxy
curl http://localhost:3001/health

# Test competitor analysis connection
curl http://localhost:3001/test-competitor-analysis
```

### Debug Mode

To enable debug logging, set the environment variable:
```bash
export DEBUG=1
```

## 📚 API Documentation

Once the backend services are running, visit these URLs for interactive API documentation:

- **Content Generator**: http://localhost:8001/docs
- **Competitor Analysis**: http://localhost:8002/docs
- **Node.js Proxy**: http://localhost:3001/health (health check only)

## 🔄 Updates Made

### Backend Changes
- **Content Generator**: Added `ContentGenerationRequest` model for frontend requests
- **Content Generator**: Created `/api/ai-writer/generate-content` endpoint
- **Content Generator**: Integrated with existing LLM client for content generation
- **Content Generator**: Added SEO scoring and prediction logic
- **Content Generator**: Enhanced response structure for frontend compatibility
- **Competitor Analysis**: Complete competitor analysis service with SERP scraping
- **Competitor Analysis**: AI-powered predictions and strategy recommendations
- **Competitor Analysis**: Background processing with real-time status updates
- **Node.js Proxy**: Added competitor analysis endpoint routing
- **Node.js Proxy**: Enhanced health checks for all services

### Frontend Changes
- **ContentAI**: Updated API URL to point to correct backend endpoint
- **ContentAI**: Maintained existing UI/UX without breaking changes
- **ContentAI**: Preserved all existing functionality
- **CompetitorAnalysis**: Complete competitor analysis interface
- **CompetitorAnalysis**: Real-time progress tracking
- **CompetitorAnalysis**: Results visualization and strategy display

### Integration Features
- Unified API through Node.js proxy
- Real-time updates via Socket.IO
- Comprehensive error handling
- Service health monitoring
- Automated startup scripts

## 🎉 Success!

Your SEO project now includes both Content Generation and Competitor Analysis features:

### ✅ Content Generation
- ContentAI.jsx frontend is connected to the backend generator service
- "Generate SEO Content" button generates real SEO-optimized content using AI
- Complete with SEO scores, predictions, and posting schedules

### ✅ Competitor Analysis  
- CompetitorAnalysis.jsx frontend is connected to the competitor analysis service
- "Start Analysis" button performs comprehensive competitor research
- Includes SERP analysis, competitor detection, AI predictions, and strategy recommendations

### ✅ Full Integration
- All services work together through the Node.js proxy
- Real-time updates and progress tracking
- Comprehensive error handling and health monitoring
- Easy startup with automated scripts

Your SEO project is now a complete competitor analysis and content generation platform!

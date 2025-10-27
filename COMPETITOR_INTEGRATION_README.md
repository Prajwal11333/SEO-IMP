# Competitor Analysis Integration

This document describes the integration of the Competitor Analysis feature into the SEO project.

## Overview

The Competitor Analysis feature provides AI-powered competitor tracking, ranking predictions, and strategy recommendations. It consists of:

- **Frontend**: React component (`CompetitorAnalysis.jsx`)
- **Backend**: Python FastAPI service (`Competitor/` folder)
- **Proxy**: Node.js server integration (`Server.js`)

## Architecture

```
Frontend (React) 
    ↓ HTTP requests
Node.js Proxy (port 3001)
    ↓ Proxy requests
Python Competitor Service (port 8002)
    ↓ Uses
Competitor Analysis Engine
```

## Services

### 1. Frontend (React)
- **File**: `seoz-frontend/src/components/CompetitorAnalysis.jsx`
- **Port**: 5173 (Vite dev server)
- **Features**:
  - Domain input and keyword analysis
  - Analysis depth selection (Quick/Standard/Deep)
  - Real-time progress tracking
  - Results visualization

### 2. Node.js Proxy Server
- **File**: `backend/node-server/node-Server/Server.js`
- **Port**: 3001
- **Features**:
  - Proxies competitor analysis requests
  - Handles CORS
  - Real-time updates via Socket.IO
  - Health checks for all services

### 3. Python Competitor Analysis Service
- **File**: `backend/node-server/python-service/Competitor/app.py`
- **Port**: 8002
- **Features**:
  - SERP scraping and analysis
  - Competitor detection and tracking
  - AI-powered predictions
  - Strategy recommendations
  - Background processing

## API Endpoints

### Competitor Analysis

#### Start Analysis
```http
POST /api/competitor-analysis/analyze
Content-Type: application/json

{
  "your_domain": "https://example.com",
  "keywords": ["seo tools", "analytics", "marketing"],
  "competitors": ["competitor1.com", "competitor2.com"], // optional
  "depth": 20 // 5, 10, or 20
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

#### Check Analysis Status
```http
GET /api/competitor-analysis/status/{analysis_id}
```

**Response:**
```json
{
  "analysis_id": "ca_20241201_143022",
  "status": "completed",
  "progress": 100,
  "current_step": "Completed!",
  "results": {
    "your_domain": "https://example.com",
    "keywords": ["seo tools", "analytics"],
    "competitors": ["competitor1.com", "competitor2.com"],
    "summary": {
      "total_keywords": 3,
      "competitors_analyzed": 2,
      "opportunities_found": 5
    }
  }
}
```

### Additional Endpoints

- `GET /api/competitor-analysis/serp` - Get SERP data
- `GET /api/competitor-analysis/rankings/{domain}` - Get domain rankings
- `POST /api/competitor-analysis/predictions` - Get AI predictions
- `POST /api/competitor-analysis/strategy` - Get strategy recommendations
- `GET /api/competitor-analysis/insights/{competitor_domain}` - Get competitor insights

## Installation & Setup

### 1. Install Python Dependencies

```bash
cd backend/node-server/python-service/Competitor
pip install -r requirements.txt
```

### 2. Start Services

#### Option A: Use the startup script
```bash
# Windows
start_server_test.bat

# Or manually start each service
```

#### Option B: Start services individually

**Start Competitor Analysis Service:**
```bash
cd backend/node-server/python-service/Competitor
python app.py
# or
python start_competitor_service.py
# or (Windows)
start_competitor_service.bat
```

**Start Node.js Proxy:**
```bash
cd backend/node-server/node-Server
node Server.js
```

**Start Frontend:**
```bash
cd seoz-frontend
npm run dev
```

### 3. Verify Services

Check that all services are running:

- **Frontend**: http://localhost:5173
- **Node Proxy**: http://localhost:3001/health
- **Competitor Analysis**: http://localhost:8002/health

## Usage

### 1. Access Competitor Analysis

1. Open the frontend application
2. Navigate to the Competitor Analysis tab
3. Enter your domain and keywords
4. Select analysis depth
5. Click "Start Analysis"

### 2. Monitor Progress

The frontend will show real-time progress updates:
- Scraping SERP data
- Identifying competitors
- Analyzing competitors
- Generating predictions
- Creating strategies

### 3. View Results

Once complete, you'll see:
- Summary statistics
- Top competitors list
- Detailed analysis results
- Strategy recommendations

## Features

### Analysis Depth Options

- **Quick** (5 results): ~2 minutes
- **Standard** (10 results): ~5 minutes  
- **Deep** (20 results): ~10 minutes

### AI-Powered Insights

- **Competitor Detection**: Automatically finds top competitors
- **Ranking Predictions**: Forecasts future ranking changes
- **Strategy Recommendations**: Actionable SEO strategies
- **Gap Analysis**: Identifies content and keyword opportunities

### Real-time Processing

- Background task processing
- Progress tracking
- Status updates
- Error handling

## Data Storage

The competitor analysis service uses JSON-based storage:

- `data/analyses.json` - Analysis results
- `data/tracking.json` - Tracking configurations
- `data/history.json` - Historical data

## Error Handling

The system includes comprehensive error handling:

- Service availability checks
- Connection timeout handling
- Graceful degradation
- User-friendly error messages

## Development

### Adding New Features

1. **Backend**: Add endpoints to `app.py`
2. **Proxy**: Add routes to `Server.js`
3. **Frontend**: Update `CompetitorAnalysis.jsx`

### Testing

Test individual components:

```bash
# Test competitor analysis service
curl http://localhost:8002/health

# Test proxy
curl http://localhost:3001/test-competitor-analysis

# Test analysis
curl -X POST http://localhost:3001/api/competitor-analysis/analyze \
  -H "Content-Type: application/json" \
  -d '{"your_domain":"https://example.com","keywords":["seo"]}'
```

## Troubleshooting

### Common Issues

1. **Service not starting**: Check Python dependencies
2. **Connection refused**: Verify ports are available
3. **Analysis fails**: Check SERP scraping limits
4. **Frontend errors**: Verify API endpoints

### Logs

Check service logs for debugging:
- Node.js: Console output
- Python: Terminal output
- Frontend: Browser console

## Integration Notes

- The competitor analysis is fully integrated with the existing SEO project
- No changes to existing functionality
- Uses the same Node.js proxy pattern
- Maintains consistent API structure
- Includes comprehensive error handling

## Future Enhancements

- Database integration (PostgreSQL/MongoDB)
- Advanced ML models for predictions
- Real-time competitor monitoring
- Automated reporting
- Integration with SEO tools APIs

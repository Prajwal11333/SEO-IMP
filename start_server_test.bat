@echo off
echo ======================================================================
echo 🚀 STARTING SEO BACKEND SERVICES
echo ======================================================================
echo.

echo 📁 Activating virtual environment...
cd "backend\node-server\python-service"
call venv\Scripts\activate.bat

echo.
echo 🔍 Testing services...

echo Testing Content Generator...
cd generator
python -c "import app; print('✅ Content Generator imported successfully')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Content Generator import failed
    echo    Installing dependencies...
    pip install -r requirements.txt
)

echo Testing Competitor Analysis...
cd ..\Competitor
python -c "import app; print('✅ Competitor Analysis imported successfully')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ Competitor Analysis import failed
    echo    Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo ======================================================================
echo 🚀 STARTING ALL SERVICES
echo ======================================================================
echo.
echo 📝 Services will start on:
echo    ✅ Node.js Proxy: http://localhost:3001
echo    ✅ Content Generator: http://localhost:8001
echo    ✅ Competitor Analysis: http://localhost:8002
echo.
echo Press Ctrl+C to stop all services
echo ======================================================================
echo.

echo Starting Content Generator (port 8001)...
start "Content Generator" cmd /k "cd generator && python app.py"

timeout /t 2 /nobreak >nul

echo Starting Competitor Analysis (port 8002)...
start "Competitor Analysis" cmd /k "cd Competitor && python app.py"

timeout /t 2 /nobreak >nul

echo Starting Node.js Proxy Server (port 3001)...
cd ..\node-Server
start "Node Proxy" cmd /k "node Server.js"

echo.
echo ✅ All services started!
echo.
echo 📋 Service URLs:
echo    🌐 Frontend: http://localhost:5173
echo    🔗 Node Proxy: http://localhost:3001
echo    📝 Content Generator: http://localhost:8001
echo    🔍 Competitor Analysis: http://localhost:8002
echo.
echo Press any key to exit...
pause >nul

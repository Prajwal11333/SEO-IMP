import sys
import py_compile

try:
    py_compile.compile(r'c:\Users\DELL INS 5510\Desktop\try\backend\node-server\python-service\generator\app.py', doraise=True)
    print("✅ Backend app.py syntax is valid")
    sys.exit(0)
except py_compile.PyCompileError as e:
    print(f"❌ Syntax error in app.py: {e}")
    sys.exit(1)

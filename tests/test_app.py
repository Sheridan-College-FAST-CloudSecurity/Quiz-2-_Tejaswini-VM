import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def test_hello():
       response = app.test_client().get('/')
       #adsfasf
       assert response.status_code == 200
       assert response.data == b"Hello, DevSecOps!"
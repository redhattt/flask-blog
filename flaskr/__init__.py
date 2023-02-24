#!/usr/bin/python3

import os
from flask import Flask

def create_app(test_config = None):
    app = Flask(__name__)
    
    @app.route('/')
    def ping():
        return {"ping": "pong"}
    
    return app
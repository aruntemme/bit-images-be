from flask import Flask, jsonify
# from bson import json_util
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Hello"


@app.route('/images')
def index():
    data = [{
        "imageUrl": "https://images.unsplash.com/photo-1667506609659-599fb1f59f94?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=929&q=80",
        "likes": 50,
    },
    {
        "imageUrl": "https://media.giphy.com/media/3o7TKsQ8gqVrXwXWZK/giphy.gif",
        "likes": 0,
    },
    
    ]
    response = jsonify(data)
    return response
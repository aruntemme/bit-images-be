from flask import Flask, jsonify
from bson import json_util
from pymongo import MongoClient
import urllib 
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# update this below line with monogdb cluster URL
client = MongoClient(url)
db = client.gifs
images = db.images

@app.route('/images')
def index():
    all_images = list(images.find())
    print(all_images)
    response = json_util.dumps(all_images)
    return response

# @app.route('/images/add', methods = ['POST'])
# def addImages():
    


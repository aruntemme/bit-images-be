from pymongo import MongoClient
import urllib 

client = MongoClient("mongodb+srv://admin:"+ urllib.parse.quote("admin@123")+"@database.roxntvt.mongodb.net/?retryWrites=true&w=majority")
db = client.gifs


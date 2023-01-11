from flask import Flask
from flask_pymongo import PyMongo
def connection():
   app = Flask(__name__)
   app.secret_key="secretkey"
   app.config['MONGO_URI']="mongodb://localhost:27017/npkdatabase"
   mongo=PyMongo(app)
   return mongo
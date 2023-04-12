from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DATABASE = os.environ.get('DATABASE')

# mongoDB 연결
from pymongo import MongoClient

mongo = MongoClient(HOST, int(PORT), connect=False)

# DataBase 접근
db = mongo[DATABASE]

# Collection 접근
accounts_collection = db.accounts
patients_collection = db.patients

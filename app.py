import json

import requests
from flask import jsonify

import login_signup
def adding_user(user_information):
   api_url = "http://127.0.0.1:5000/add"
   headers = {"Content-Type": "application/json"}
   user_data = {"name": user_information[0],
               "email": user_information[1],
               "age": user_information[2],
               "phonenumber": user_information[3],
               "password": user_information[4],
               "fieldOwned": user_information[5]
               }
   response = requests.post(api_url, data=json.dumps(user_data), headers=headers)
   response.json()


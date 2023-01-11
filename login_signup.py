import json
import jwt
import api
import config
import requests

import crop_details

mongo=config.connection()

def login_signup(input_selection):
    # todo get jwt from header
    # decode jwt
    #
    if input_selection==2:
         user_name=(str(input("Enter your name:")))
         user_emailid=(str(input("Enter your unique Email Id :")))
         user_age=(int(input("Enter your age:")))
         user_phonenumber=(int(input("Enter your phone number:")))
         user_password=(str(input("Enter your password:")))
         user_fieldOwned=(str(input("Enter the Fields you Own seperated by a space :")))

         api_url = "http://127.0.0.1:5000/add"
         headers = {"Content-Type": "application/json"}
         user_data = {"name": user_name,
                      "email": user_emailid,
                      "age": user_age,
                      "phonenumber": user_phonenumber,
                      "password": user_password,
                      "fieldOwned": user_fieldOwned
                      }
         response = requests.post(api_url, data=json.dumps(user_data), headers=headers)
         response.json()

         login_signup(1)

    elif input_selection==1:
        Email_id=input("Enter your Email id to login :")
        password=input("Enter your password here :")
        x=0
        for x in mongo.db.user_details.find({"email":Email_id,"password":password}):
           x=1
        if x:
            print("You are Logged in ")
            # encoded = jwt.encode({"email":"testuser","password":"user@123" }, "secret", algorithm="HS256")
            # print(encoded)
            crop_details.cropoperation(Email_id)
        else:
            print("Please enter a Valid Password")
    elif input_selection==3:
        Email_id = input("Enter your Email id to Delete it :")
        print("If you want to delete this Email id, then enter 1 :")
        y=int(input())
        if( y==1):
            delete=api.delete_plants(Email_id)
            print(delete,"Deleted successfully")
        else:
            print("User not Deleted")


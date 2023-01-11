import config
from middleware import authentication_middleware
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask,request,jsonify
app=Flask(__name__)
mongo=config.connection()

@app.route('/')
@authentication_middleware
def view_user():
        view_user=mongo.db.user_details.find()
        resp=dumps(view_user)
        return resp
@app.route('/add',methods=['POST'])
def add_user():
         _json=request.json
         _name=_json['name']
         _email=_json['email']
         _age=_json['age']
         _phonenumber=_json['phonenumber']
         _password=_json['password']
         _fieldOwned=_json['fieldOwned']
         if _name and _age and _email and _phonenumber and _password and request.method=='POST':
              id = mongo.db.user_details.insert_one({'name':_name,'email':_email,'age':_age,'phonenumber':_phonenumber,'password':_password,'fieldOwned':_fieldOwned})

              resp=jsonify("user added successfully")

              resp.status_code=200
              return resp
         else:
              return not_found()
@app.route('/plants')
def plants(email):
    plants=mongo.db.user_details.find({"email":email})
    resp=dumps(plants)
    return resp
@app.route('/plant/<id>')
def plant(id):
         plant=mongo.db.values.find_one({'_id':ObjectId(id)})
         resp=dumps(plant)
         return resp
    # @app.route('/put', methods=['PUT'])
    # def editUserId():
    #         _json = request.json
    #         _email = _json["email"]
    #         _name = _json["name"]
    #         _age = _json["age"]
    #         _phonenumber = _json["phonenumber"]
    #         _password = _json["password"]
    #         _fieldOwned = _json['fieldOwned']
    #         update_user_id(_email,_name,_age,_phonenumber,_password,_fieldOwned)
    #
    #         return {"message": "Updated Successfully"}
    #
    # def update_user_id(_email,_name,_age,_phonenumber,_password,_fieldOwned):
    #         data=mongo.db.user_details.find_one({"email":_email})
    #         new_data={ "$set": {"name":_name,
    #                             "age":_age,
    #                             "phonenumber":_phonenumber,
    #                             "password":_password,
    #                             "fieldOwned":_fieldOwned
    #                             }   }
    #         mongo.db.update_one(data,new_data)
@app.route('/delete',methods=['DELETE'])
def delete_plants(email):
         mongo.db.user_details.delete_one({"email":email})
         resp=jsonify("user deleteded sucessfully ")
         resp.status_code=200
         return resp
@app.errorhandler(404)
def not_found(error=None):
         message={
              'status':404,
              'message':'nooot found'+request.url
         }
         resp=jsonify(message)

         resp.status_code=404
         return resp



if __name__=='__main__':
     app.run(debug=True)

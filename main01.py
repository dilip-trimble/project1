from flask import Flask
from flask_restful import Api
from flask import request
from database import *

app = Flask(__name__)
api = Api(app)




@app.route('/getCropData', methods=['GET'])
def getCropData():
        req = request.json
        data = read_crop_data(req["crop_name"])
        return data


@app.route('/postCropData', methods=['POST'])
def postCropData():
        data = request.json
        crop_name = data["crop_name"]
        nitrogen_level = data["nitrogen_level"]
        phosphorus_level = data["phosphorus_level"]
        potassium_level = data["potassium_level"]


        create_new_crop_data(crop_name, nitrogen_level, phosphorus_level, potassium_level)

        return {"message": "Created Successfully"}


@app.route('/putCropData', methods=['PUT'])
def putCropData():
        data = request.json
        crop_name = data["crop_name"]
        nitrogen_level = data["nitrogen_level"]
        phosphorus_level = data["phosphorus_level"]
        potassium_level = data["potassium_level"]
        update_crop_data(crop_name, nitrogen_level, phosphorus_level, potassium_level)

        return {"message": "Updated Successfully"}

@app.route('/deleteCropData', methods=['DELETE'])
def deleteCropData():
        data = request.json
        crop_name = data["crop_name"]
        delete_crop_data(crop_name)

        return {"message": "Deleted Successfully"}

if __name__ == "__main__":
    app.run(debug=True)

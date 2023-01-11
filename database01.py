from pymongo import MongoClient

myClient = MongoClient("mongodb://localhost:27017")
myDb = myClient["Project"]

crop_collection = myDb["Crops"]


def create_new_crop_data(crop_name, nitrogen_level, phosphorus_level, potassium_level):
    data = {"crop_name": crop_name,
            "nitrogen_level": nitrogen_level,
            "phosphorus_level": phosphorus_level,
            "potassium_level": potassium_level
            }

    crop_collection.insert_one(data)


def read_crop_data(crop_name):
    data = crop_collection.find_one()
    return {"crop_name": data["crop_name"],
            "nitrogen_level": data["nitrogen_level"],
            "phosphorus_level": data["phosphorus_level"],
            "potassium_level": data["potassium_level"]
            }


def update_crop_data(crop_name, nitrogen_level, phosphorus_level, potassium_level):
    data = crop_collection.find_one({"crop_name": crop_name})
    new_data = {"$set": {"nitrogen_level": nitrogen_level,
                         "phosphorus_level": phosphorus_level,
                         "potassium_level": potassium_level
                         }}
    crop_collection.update_one(data, new_data)


def delete_crop_data(crop_name):
    data = {"crop_name": crop_name}
    crop_collection.delete_one(data)



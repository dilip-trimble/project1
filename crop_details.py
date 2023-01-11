import json

import api
import config
mongo=config.connection()
def cropoperation(email):
    response=api.plants(email)
    resp= json.loads(response);
    print(resp[0]['fieldOwned'],"Please select your field that you want to soil test")
    field_name=input();






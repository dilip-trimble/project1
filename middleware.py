from functools import wraps
jwt_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3R1c2VyIiwicGFzc3dvcmQiOiJ1c2VyQDEyMyJ9.Gj6PHAJToHDGJseFMqO7nXOy9n3uXaRwS-vvACr_79s"
import jwt
from flask import request,Response

def authentication_middleware(func):
    @wraps(func)
    def decorated_function(*args,**kwargs):
         access_i = jwt.decode(jwt_token, "secret", algorithms=["HS256"])
         print(access_i['email'],access_i['password'])
         username=request.authorization[access_i['email']]
         password=request.authorization[access_i['password']]

         if username=="testuser"and password=="user@123":
             return func(*args,**kwargs)
         return Response('Authorization failed',mimetype="text/plain",status=401)
    return decorated_function
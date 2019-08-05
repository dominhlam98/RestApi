from fastapi import FastAPI
from pymongo import MongoClient
from models import Passenger
from starlette.status import *
from starlette.responses import Response
import json

app = FastAPI(debug=True)


HOST = 'localhost'
PORT = 27017
DATABASE_NAME = 'API'
COLLECTION_NAME = 'Passenger'

# set host and port to mongodb
client = MongoClient(host=HOST, port=PORT)

# set database name
db = client[DATABASE_NAME]

# set collection name
cn = db[COLLECTION_NAME]


@app.post('/passenger/')
async def create_passenger(passenger: Passenger, response: Response):
    data = cn.find_one({'phone': passenger.phone})
    if data is not None:
        response.status_code = HTTP_400_BAD_REQUEST
        return {'message': 'this phone number already exist'}
    cn.insert_one(passenger.convert_json())
    response.status_code = HTTP_201_CREATED
    return {'message': 'create success'}


@app.get('/passenger/{phone:str}')
async def get_passenger(phone: str, response: Response):
    data = cn.find_one({'phone': phone})
    if data is None:
        response.status_code = HTTP_404_NOT_FOUND
        return {'message': 'cannot find'}
    else:
        response.status_code = HTTP_200_OK
        return{
            'fullname': data['fullname'],
            'phone': data['phone'],
            'email': data['email'],
            'score': data['score']
        }


@app.get('/passenger/')
async def get_all():
    data = cn.find({}, {'_id': 0})
    lst_data = []
    for p in data:
        lst_data.append(p)
    return lst_data


@app.put('/passenger/{phone:str}')
async def modify_passenger(phone: str, passenger: Passenger):
    cn.find_one_and_update({'phone': phone}, {'$set': passenger.convert_json()})
    return passenger.convert_json()

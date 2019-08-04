from pymongo import MongoClient
from fastapi import FastAPI
from models import Passenger

# set host and port
client = MongoClient(host='localhost', port=27017)
# set database name client['database name']
db_name = client['graphene-mongo-example']
# set collection name db_name['collection name']
db = db_name['passenger']

# use FastAPI
app = FastAPI()


@app.post('/passengers/')
def create_passenger(passenger: Passenger):
    db.insert_one(passenger.json())
    return {
        passenger.json()
    }


@app.get('/passengers/{email}')
def get_passenger(email: str):
    passenger = db.find_one({'email': email})
    return {
        'fullname': passenger['fullname'],
        'phone': passenger['phone'],
        'email': passenger['email'],
        'created': passenger['created']
    }


@app.put('/passengers/{email}')
def modify_passenger(email:str, passenger:Passenger):
    db.find_one_and_update({'email': email}, {'$set': passenger.json()})
    return{
        passenger.json()
    }

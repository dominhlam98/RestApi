import datetime
from pydantic import BaseModel
from pydantic.types import EmailStr


class Passenger(BaseModel):
    fullname: str
    phone: str
    email: EmailStr
    score: int
    created: datetime.date

    def convert_json(self):
        return {
            'fullname': self.fullname,
            'phone': self.phone,
            'email': self.email,
            'score': self.score,
            'created': datetime.datetime.now()
        }

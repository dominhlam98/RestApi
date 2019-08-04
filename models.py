from pydantic import BaseModel
import datetime


class Passenger(BaseModel):
    fullname: str
    phone: str
    email: str
    score: int = 0

    def convert_json(self):
        return {
            'fullname': self.fullname,
            'phone': self.phone,
            'email': self.email,
            'score': self.score,
            'created': datetime.datetime.date()
        }
from datetime import datetime
import re


class ParkedCar:
    def __init__(self, code: str, plate: str, date: datetime):
        if not re.match(r'[A-Z]{3}-[0-9]{4}', plate):
            raise Exception('Invalid Plate')

        self.code = code
        self.plate = plate
        self.date = date

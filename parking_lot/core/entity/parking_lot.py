from datetime import datetime


class ParkingLot:
    def __init__(self,
                 code: str,
                 capacity: int,
                 open_hour: int,
                 close_hour: int,
                 occupied_spaces: int):
        self.code = code
        self.capacity = capacity
        self.open_hour = open_hour
        self.close_hour = close_hour
        self.occupied_spaces = occupied_spaces

    def is_open(self, date: datetime):
        return self.open_hour < date.hour < self.close_hour

    def is_full(self):
        return self.capacity == self.occupied_spaces

    def __repr__(self):
        return f'\nCode: {self.code}, Capacity: {self.capacity}, ' \
               f'Open: {self.open_hour}, Close: {self.close_hour}, ' \
               f'Occupied: {self.occupied_spaces}'

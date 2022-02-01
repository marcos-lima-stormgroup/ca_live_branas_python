from datetime import datetime

from parking_lot.core.adapter.parking_lot_adapter import ParkingLotAdapter
from parking_lot.core.entity.parking_lot import ParkingLot
from parking_lot.core.repository.parking_lot_repository import \
    ParkingLotRepository


class ParkingLotRepositoryMemory(ParkingLotRepository):
    def __init__(self):
        self.parking_lots = {
            "shopping": {"code": "shopping",
                         "capacity": 45,
                         "open_hour": 8,
                         "close_hour": 22,
                         "occupied_spaces": 0}
        }
        self.parked_cars = dict()

    def get(self, code) -> ParkingLot:
        parking_lot_data = self.parking_lots[code]
        occupied_spaces = len(self.parked_cars)
        parking_lot = ParkingLotAdapter.create(parking_lot_data['code'],
                                               parking_lot_data['capacity'],
                                               parking_lot_data['open_hour'],
                                               parking_lot_data['close_hour'],
                                               occupied_spaces)
        return parking_lot

    def save_parked_car(self, code: str, plate: str, date: datetime):
        self.parked_cars[code] = {'code': code, 'plate': plate, 'date': date}

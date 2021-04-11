from datetime import datetime

from parking_lot.core.entity.parked_car import ParkedCar
from parking_lot.core.repository.parking_lot_repository import \
    ParkingLotRepository


class EnterParkingLotInteractor:
    def __init__(self, parking_lot_repository: ParkingLotRepository):
        self.parking_lot_repository = parking_lot_repository

    def run(self, code: str, plate: str, date: datetime):
        parking_lot = self.parking_lot_repository.get(code)
        parked_car = ParkedCar(code, plate, date)

        if not parking_lot.is_open(parked_car.date):
            raise Exception('The parking lot is closed')

        if parking_lot.is_full():
            raise Exception('The parking lot is full')

        self.parking_lot_repository.save_parked_car(parked_car.code,
                                                    parked_car.plate,
                                                    parked_car.date)
        return parking_lot

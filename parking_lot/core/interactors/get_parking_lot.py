from parking_lot.core.entity.parking_lot import ParkingLot
from parking_lot.core.repository.parking_lot_repository import \
    ParkingLotRepository


class GetParkingLotInteractor:
    def __init__(self, parking_lot_repository: ParkingLotRepository):
        self.parking_lot_repository = parking_lot_repository

    def run(self, code: str) -> ParkingLot:
        return self.parking_lot_repository.get(code)

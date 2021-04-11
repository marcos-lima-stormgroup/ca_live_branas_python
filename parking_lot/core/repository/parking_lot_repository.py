from abc import ABC, abstractmethod
from datetime import datetime

from parking_lot.core.entity.parking_lot import ParkingLot


class ParkingLotRepository(ABC):
    @abstractmethod
    def get(self, code: str) -> ParkingLot:
        raise NotImplementedError

    def save_parked_car(self, code: str, plate: str, date: datetime):
        raise NotImplementedError

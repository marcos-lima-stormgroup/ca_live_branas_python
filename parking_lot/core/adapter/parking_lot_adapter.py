from parking_lot.core.entity.parking_lot import ParkingLot


class ParkingLotAdapter:
    @staticmethod
    def create(code: str,
               capacity: int,
               open_hour: int,
               close_hour: int,
               occupied_spaces: int):
        return ParkingLot(code,
                          capacity,
                          open_hour,
                          close_hour,
                          occupied_spaces)

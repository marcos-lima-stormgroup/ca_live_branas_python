# from parking_lot.core.entity.parking_lot import ParkingLot
# from parking_lot.core.repository.parking_lot_repository import \
#     ParkingLotRepository
#
#
# class PostParkingLotRequestModel:
#     def __init__(self, code: str):
#         self.code = code
#
#
# class PostParkingLotInteractor:
#     def __init__(self, parking_lot_repository: ParkingLotRepository):
#         self.parking_lot_repository = parking_lot_repository
#
#     def run(self, request: GetParkingLotRequestModel) -> ParkingLot:
#         return self.parking_lot_repository.get(request.code)

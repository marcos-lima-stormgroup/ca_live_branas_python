from parking_lot.core.entity.parking_lot import ParkingLot
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotInteractor, GetParkingLotRequestModel
from parking_lot.infra.repository.parking_lot_repository_memory import \
    ParkingLotRepositoryMemory


class ParkingLotController:
    @staticmethod
    def get_parking_lot(request: GetParkingLotRequestModel) -> ParkingLot:
        repository = ParkingLotRepositoryMemory()
        get_parkinglot_interactor = GetParkingLotInteractor(repository)
        return get_parkinglot_interactor.run(request)
    #
    # @staticmethod
    # def post_parking_lot(request: PostParkingLotRequestModel) -> ParkingLot:
    #     repository = ParkingLotRepositorySql()
    #     post_parkinglot_interactor = PostParkingLotInteractor(repository)
    #     return post_parkinglot_interactor.run(request)

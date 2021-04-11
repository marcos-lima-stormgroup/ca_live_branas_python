from parking_lot.core.entity.parking_lot import ParkingLot
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotInteractor, GetParkingLotRequestModel
from parking_lot.infra.repository.parking_lot_repository_sql import \
    ParkingLotRepositorySql


class ParkingLotController:
    @staticmethod
    def get_parking_lot(request: GetParkingLotRequestModel) -> ParkingLot:
        repository = ParkingLotRepositorySql()
        get_parkinglot_interactor = GetParkingLotInteractor(repository)
        return get_parkinglot_interactor.run(request)

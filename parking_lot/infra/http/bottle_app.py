from bottle import route, run

from parking_lot.core.adapter.bottle_adapter import BottleAdapter
from parking_lot.core.controller.parking_lot_controller import \
    ParkingLotController
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotRequestModel


@route('/parkingLots/<code>')
def get_parking_lot(code):
    get_request = GetParkingLotRequestModel(code)
    return BottleAdapter.handle_get(
        ParkingLotController.get_parking_lot)(get_request)


if __name__ == '__main__':
    run(host='localhost', port=8050)

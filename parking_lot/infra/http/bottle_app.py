from bottle import route, run

from parking_lot.core.adapter.bottle_adapter import BottleAdapter
from parking_lot.core.controller.parking_lot_controller import \
    ParkingLotController
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotRequestModel


@route('/parkingLots/<code>')
def get_parking_lot(code):
    get_request = GetParkingLotRequestModel(code)
    response = BottleAdapter.handle_get(
        ParkingLotController.get_parking_lot)(get_request)

    return {"code": response.code,
            "capacity": response.capacity,
            "open_hour": response.open_hour,
            "close_hour": response.close_hour,
            "occupied_spaces": response.occupied_spaces}


if __name__ == '__main__':
    run(host='localhost', port=8000)

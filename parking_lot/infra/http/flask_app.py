from flask import Flask

from parking_lot.core.adapter.flask_adapter import FlaskAdapter
from parking_lot.core.controller.parking_lot_controller import \
    ParkingLotController
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotRequestModel

app = Flask(__name__)


@app.route('/')
def entry_point():
    return 'Hello World!'

#
# @app.route('/parkingLots/<code>')
# def get_parkinglot_by_id(code):
#     repository = ParkingLotRepositorySql()
#     get_parkinglot_interactor = GetParkingLotInteractor(repository)
#
#     parking_lot = get_parkinglot_interactor.run(code)
#
#     return {"code": parking_lot.code,
#             "capacity": parking_lot.capacity,
#             "open_hour": parking_lot.open_hour,
#             "close_hour": parking_lot.close_hour,
#             "occupied_spaces": parking_lot.occupied_spaces}
#


@app.route('/parkingLots/<code>')
def get_parkinglot_by_id(code):
    get_request = GetParkingLotRequestModel(code)
    response = FlaskAdapter.handle_get(
        ParkingLotController.get_parking_lot)(get_request)

    return {"code": response.code,
            "capacity": response.capacity,
            "open_hour": response.open_hour,
            "close_hour": response.close_hour,
            "occupied_spaces": response.occupied_spaces}


if __name__ == '__main__':
    app.run(debug=True)

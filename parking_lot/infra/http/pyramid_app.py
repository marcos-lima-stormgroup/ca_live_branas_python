from wsgiref.simple_server import make_server

from pyramid.config import Configurator

from parking_lot.core.adapter.pyramid_adapter import PyramidAdapter
from parking_lot.core.controller.parking_lot_controller import \
    ParkingLotController
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotRequestModel


def get_parking_lots(request):
    get_request = GetParkingLotRequestModel(request.matchdict['code'])
    response = PyramidAdapter.handle_get(
        ParkingLotController.get_parking_lot)(get_request)

    return response


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('GetParkingLots', '/parkingLots/{code}')
        config.add_view(get_parking_lots, route_name='GetParkingLots')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

import sys

from parking_lot.core.adapter.cli_adapter import CliAdapter
from parking_lot.core.controller.parking_lot_controller import \
    ParkingLotController
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotRequestModel

if __name__ == '__main__':
    # Teste para pull-request intra repo.
    print('CLI Parking Lot')
    try:
        if sys.argv[1] == 'get_parking_lot':
            code = sys.argv[2]
            get_request = GetParkingLotRequestModel(code)
            response = CliAdapter.handle_get(
                ParkingLotController.get_parking_lot)(get_request)

            print(response)
    except IndexError as e:
        print('Passe parametros!')

    print('Done')

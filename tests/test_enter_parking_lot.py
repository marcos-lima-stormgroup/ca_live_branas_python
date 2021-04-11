from datetime import datetime
from unittest import TestCase

from _pytest.python_api import raises

from parking_lot.core.interactors.enter_parking_lot_interactor import \
    EnterParkingLotInteractor
from parking_lot.core.interactors.get_parking_lot import \
    GetParkingLotInteractor
from parking_lot.infra.repository.parking_lot_repository_memory import \
    ParkingLotRepositoryMemory


class TestParkingLot(TestCase):
    def test_should_get_parking_lot(self):
        repository = ParkingLotRepositoryMemory()
        get_interactor = GetParkingLotInteractor(repository)
        parking_lot = get_interactor.run('shopping')
        self.assertEqual(parking_lot.code, 'shopping')

    def test_should_enter_parking_lot(self):
        repository = ParkingLotRepositoryMemory()
        enter_interactor = EnterParkingLotInteractor(repository)
        get_interactor = GetParkingLotInteractor(repository)
        parking_lot_before = get_interactor.run('shopping')
        self.assertEqual(parking_lot_before.occupied_spaces, 0)

        enter_date = datetime.fromisoformat('2021-03-01T10:00:00')
        enter_interactor.run("shopping",
                             'MMM-0001',
                             enter_date)

        parking_lot_after = get_interactor.run('shopping')
        self.assertEqual(parking_lot_after.occupied_spaces, 1)

    def test_shoud_be_closed(self):
        repository = ParkingLotRepositoryMemory()
        enter_interactor = EnterParkingLotInteractor(repository)
        get_interactor = GetParkingLotInteractor(repository)
        parking_lot_before = get_interactor.run('shopping')
        self.assertEqual(parking_lot_before.occupied_spaces, 0)

        enter_date = datetime.fromisoformat('2021-03-01T23:00:00')
        with raises(Exception) as exc_info:
            enter_interactor.run("shopping", 'MMM-0001', enter_date)

        self.assertEqual(str(exc_info.value), 'The parking lot is closed')

    def test_shoud_be_full(self):
        repository = ParkingLotRepositoryMemory()
        enter_interactor = EnterParkingLotInteractor(repository)
        get_interactor = GetParkingLotInteractor(repository)
        parking_lot_before = get_interactor.run('shopping')
        self.assertEqual(parking_lot_before.occupied_spaces, 0)

        enter_date = datetime.fromisoformat('2021-03-01T10:00:00')
        enter_interactor.run("shopping", 'MMM-0001', enter_date)
        enter_interactor.run("shopping", 'MMM-0002', enter_date)
        enter_interactor.run("shopping", 'MMM-0003', enter_date)
        enter_interactor.run("shopping", 'MMM-0004', enter_date)
        enter_interactor.run("shopping", 'MMM-0005', enter_date)

        with raises(Exception) as exc_info:
            enter_interactor.run("shopping", 'MMM-0006', enter_date)

        self.assertEqual(str(exc_info.value), 'The parking lot is full')

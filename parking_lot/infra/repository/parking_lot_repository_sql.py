from datetime import datetime

from parking_lot.core.adapter.parking_lot_adapter import ParkingLotAdapter
from parking_lot.core.entity.parking_lot import ParkingLot
from parking_lot.core.repository.parking_lot_repository import \
    ParkingLotRepository
from parking_lot.infra.database.database import conn
from parking_lot.infra.repository.parking_lot_sql_queries import \
    get_parking_lots, insert_parked_car


class ParkingLotRepositorySql(ParkingLotRepository):
    def get(self, code) -> ParkingLot:
        cur = conn.cursor()
        cur.execute(get_parking_lots, (code,))
        parking_lot_data = cur.fetchone()
        return ParkingLotAdapter.create(*parking_lot_data)

    def save_parked_car(self, code: str, plate: str, date: datetime):
        cur = conn.cursor()
        cur.execute(insert_parked_car, (code, plate, date))
        conn.commit()

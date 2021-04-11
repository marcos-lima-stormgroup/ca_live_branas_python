get_parking_lots = """
select 
    *,
    (
        select 
            count(*) 
        from 
            parked_cars pc 
        where 
            pc.code = pl.code
    ) 
from 
    parking_lots pl 
where 
    pl.code = %s
"""

insert_parked_car = """
insert into parked_cars(code, plate, enter_date) values (%s, %s, %s)
"""

import os
from loo.database import init_db

init_db()

from loo.database import getsession

session = getsession()

import loo.models as models

buildings = os.listdir("maps/names/")


for building in buildings:
    theb = models.Building(building, open('maps/names/' + building ).read().strip())
    session.add(theb)
    session.commit()
    floors = os.listdir("maps/images/" + building)
    for floor in floors:
        floor = floor.split(".")[0]
        print building, floor
        thef = models.Floor(floor, theb)
        session.add(thef)
        session.commit()


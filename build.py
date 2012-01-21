import os
import flask
app = flask.Flask(__name__)
app.config['DEBUG'] = True

import loo.models as models

models.metadata.bind = 'sqlite:///sqlite.db'

models.setup_all()
models.create_all()

buildings = os.listdir("maps/names/")

for building in buildings:
    theb = models.Building(building, open('maps/names/' + building ).read().strip())
    models.session.add(theb)
    models.session.commit()
    floors = os.listdir("maps/images/" + building)
    for floor in floors:
        floor = floor.split(".")[0]
        print building, floor
        thef = models.Floor(floor, theb)
        models.session.add(thef)
        models.session.commit()


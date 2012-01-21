import flask
app = flask.Flask(__name__)
app.config['DEBUG'] = True

import models

#db_password = open('db_password').read()[:-1]
#models.metadata.bind = 'mysql://mimcpher:{0}@localhost/mimcpher'.format(db_password)
models.metadata.bind = 'sqlite:///sqlite.db'

models.setup_all()

import views

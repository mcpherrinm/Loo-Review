import flask
from loo import app
import models
import forms
from loo.database import getsession

@app.route('/')
def home():
    S = getsession()
    R = S.query(models.Review).first()
    return flask.render_template('home.html', item=R)

@app.route('/browse')
def browse():
    S = getsession()
    floors = S.query(models.Floor).all()
    foo = [{'name': str(x).replace(',', ' '), 'url': str(x).replace(',','/')} for x in floors]
    return flask.render_template('browse.html', floors=foo)

@app.route('/all')
def listall():
    S = getsession()
    Rs = S.query(models.Review).all()
    return flask.render_template('list.html', content=Rs)

@app.route('/review', methods=['GET', 'POST'])
def review():
    form = forms.AddReviewForm(flask.request.form)
    if flask.request.method == "POST":
        if form.validate():
            thereview = models.Review(form.room.data, form.description.data, form.rank.data)
            shesh = getsession.object_session(thereview)
            shesh.commit()
            return "Success, <a href='../'>back</a>"
    return flask.render_template('submit.html', form=form)

@app.route('/browse/<building>/<floor>')
def showfloor(building, floor):
  S = getsession()
  findfloor = S.query(models.Floor).filter(models.Floor.name == floor).join(models.Building).filter(models.Building.name == building).all()
  R = S.query(models.Room).join(models.Floor).filter(models.Floor.name == floor).all()
  rooms = [{'name': str(x),'url': "/room/MC/" + x.name, 'mapY': x.mapy, 'mapX': x.mapx} for x in R]
  return flask.render_template('floor.html', rooms = rooms, imageurl ="http://csclub.uwaterloo.ca/~mimcpher/loo/maps/images/"+building+"/"+floor+".png")

@app.route('/room/<building>/<room>')
def show(building, room):
   S = getsession()
   R = S.query(models.Review).join(models.Room).filter(models.Room.name == room).all()
   return flask.render_template('list.html', content = R)

@app.route('/room/new', methods=['GET', 'POST'])
def room():
    form = forms.AddRoom(flask.request.form)
    if flask.request.method == "POST":
        if form.validate():
            theroom = models.Room(form.name.data, form.gender.data, form.floor.data,
              form.mapx.data, form.mapy.data)
            S = getsession.object_session(theroom)
            S.commit()
            return "Valid New Room"
    return flask.render_template('newroom.html', form=form)


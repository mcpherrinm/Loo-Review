import flask
from loo import app
import models
import forms
from loo.database import getsession


@app.route('/')
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


import flask
from loo import app
import models
import forms

@app.route('/')
def listall():
    return flask.render_template('list.html', content=models.session.query(models.Review).all())

@app.route('/review', methods=['GET', 'POST'])
def review():
    form = forms.AddReviewForm(flask.request.form)
    if flask.request.method == "POST":
        if form.validate():
            thereview = models.Review(form.room.data, form.description.data, form.rank.data)
            models.session.commit()
            return "Success, <a href='../'>back</a>"
    return flask.render_template('submit.html', form=form)

@app.route('/room/new', methods=['GET', 'POST'])
def room():
    form = forms.AddRoom(flask.request.form)
    if flask.request.method == "POST":
        if form.validate():
            theroom = models.Room(form.name.data, form.floor.data,
              form.mapx.data, form.mapy.data)
            models.session.add(theroom)
            models.session.commit()
            return "Valid New Room"
    return flask.render_template('newroom.html', form=form)

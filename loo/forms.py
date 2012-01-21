from wtforms import fields, validators, Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import models

class AddReviewForm(Form):
    description = fields.TextAreaField(validators=[validators.Length(min=100)])
    room        = fields.TextField(u'Room') #QuerySelectField(query_factory=models.session.query(models.Room).all)
    rank        = fields.IntegerField(validators=[validators.NumberRange(1, 5)])

class AddRoom(Form):
    name  = fields.TextField(u'Room Number', [validators.required(), validators.length(max=20)])
    building = fields.TextField(u'Building') #QuerySelectField(query_factory=models.session.query(models.Building).all)
    floor = fields.TextField(u'floor') #QuerySelectField(query_factory=models.session.query(models.Floor).all)
    gender = fields.RadioField(choices= [('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')])
    mapx  = fields.IntegerField(validators=[validators.Optional()])
    mapy  = fields.IntegerField(validators=[validators.Optional()])

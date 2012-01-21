from wtforms import fields, validators, Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import models

class AddReviewForm(Form):
    description = fields.TextAreaField(validators=[validators.Length(min=100)])
    room        = QuerySelectField(query_factory=models.session.query(models.Room).all)
    rank        = fields.IntegerField(validators=[validators.NumberRange(1, 5)])

class AddRoom(Form):
    name  = fields.TextField(u'Room Number', [validators.required(), validators.length(max=20)])
    floor = QuerySelectField(query_factory=models.session.query(models.Floor).all)
    mapx  = fields.IntegerField(validators=[validators.Optional()])
    mapy  = fields.IntegerField(validators=[validators.Optional()])

class AddFloor(Form):
    building = QuerySelectField(query_factory=models.session.query(models.Building).all)
    name = fields.TextField(u'Floor Name', [validators.Length(max=6)])

class AddBuilding(Form):
    code = fields.TextField(u'Building Code', [validators.Length(max=6)])
    name = fields.TextField(u'Building Name', [validators.Length(max=30)])

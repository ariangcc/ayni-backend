from app import db, ma
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from models.addUpdateDelete import AddUpdateDelete
from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from sqlalchemy import *
##
from models.activity import Activity
##

class Contact(AddUpdateDelete, db.Model):
	## aqui las notitas de cada tipo por cada actividad
	__tablename__='contact'
	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	activity_id = db.Column(db.Integer, ForeignKey('activity.id'), nullable=False)
	name = db.Column(db.String(100), nullable = False)
	telephone_number_1 = db.Column(db.String(20))
	telephone_number_2 = db.Column(db.String(20))
	email_1 = db.Column(db.String(50))
	email_2 = db.Column(db.String(50))
	direction = db.Column(db.String(100))
	
	@classmethod
	def addOne(self,obj):
		db.session.add(obj)
		db.session.commit()
		db.session.flush()
		return 1

#class ContactSchema(ma.Schema):
	##
	#url = ma.URLFor('api.likes_x_userresource', id='<id>', _external=True)

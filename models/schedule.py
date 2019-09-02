from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import db
from config import SECRET_KEY
from passlib.apps import custom_app_context as password_context
import re
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

ma = Marshmallow()
locales = ['es_ES', 'es']

class AddUpdateDelete():
	def add(self, resource):
		db.session.add(resource)
		return db.session.commit()
	
	def update(self):
		return db.session.commit()
	
	def delete(self, resource):
		db.session.delete(resource)
		return db.session.commit()

''' Schedule '''

class Schedule(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(1000))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)
	activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

class ScheduleSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	description = fields.String(required=True, validate=validate.Length(3))
	start_date = fields.DateTime(required=True)
	end_date = fields.DateTime(required=True)
	activity_id = fields.Integer(required=True)
	url = ma.URLFor('api.scheduleresource', id='<id>', _external=True)

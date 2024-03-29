from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Email, Length
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import db, ma
from config import SECRET_KEY
from passlib.apps import custom_app_context as password_context
import re
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from models.addUpdateDelete import AddUpdateDelete
from models.project import Project

''' Activity '''
locales = ['es_ES', 'es']

class Activity(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key = True)
	title = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(1000))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)

	@classmethod
	def is_unique(cls, id, title):
		existing_activity = cls.query.filter_by(title=title).first()
		if existing_activity is None:
			return True
		else:
			if existing_activity.id == id:
				return True
			else:
				return False
	@classmethod
	def addOne(self,obj):
		db.session.add(obj)
		db.session.commit()
		db.session.flush()
		return 1
	
class ActivitySchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	title = fields.String(required=True, validate=validate.Length(3))
	description = fields.String(required=True, validate=validate.Length(3))
	latitude = fields.Float(required=True)
	longitude = fields.Float(required=True)
	user_id = fields.Integer(required=True)
	type_id = fields.Integer(required=True)
	news = fields.Nested("NewsSchema", many=True, exclude=("activity",))
	schedules = fields.Nested("ScheduleSchema", many=True, exclude=("activity",))
	enrollments = fields.Nested("EnrollmentSchema", many=True, exclude=("activity",))
	url = ma.URLFor('api.activityresource', id='<id>', _external=True)

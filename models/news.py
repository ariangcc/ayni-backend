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

''' News '''
locales = ['es_ES', 'es']

class News(AddUpdateDelete, db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key = True)
	title = db.Column(db.String(100))
	description = db.Column(db.String(1000))
	
class NewsSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	title = fields.String(required=True, validate=validate.Length(3))
	description = fields.String(required=True, validate=validate.Length(3))
	project_id = fields.Integer(required=True)
	url = ma.URLFor('api.newsresource', id='<id>', _external=True)
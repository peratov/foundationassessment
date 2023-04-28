from app.extensions.database import db
from datetime import datetime
from sqlalchemy import Column, Integer, String


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  
  
  


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  text = db.Column(db.Text())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

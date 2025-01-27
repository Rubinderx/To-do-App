# imports
from . import db
from datetime import datetime

# todo model class from db.model
class Todo(db.Model):
    # define columns for todo table
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300), unique=True)
    complete = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

from sqlalchemy import INTEGER, VARCHAR
from app import db


class Table(db.Model):
    __tablename__='results'
    id = db.Column(INTEGER, primary_key=True)
    level = db.Column(VARCHAR)
    value = db.Column(INTEGER)

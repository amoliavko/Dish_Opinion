from sqlalchemy import INTEGER, VARCHAR, TIMESTAMP
from app import db


class Table(db.Model):
    __tablename__='results'
    id = db.Column(INTEGER, primary_key=True)
    location = db.Column(VARCHAR)
    rating = db.Column(VARCHAR)
    data = db.Column(TIMESTAMP)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'ewevrtytevc654ygv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/dish'
db = SQLAlchemy(app)


from app import views
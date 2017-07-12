from flask import Flask

app = Flask(__name__)
app.secret_key = 'ewevrtytevc654ygv'

from app import views
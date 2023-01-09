from flask import Flask
import urllib
import pyodbc
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary


app = Flask(__name__)
app.secret_key = 'sfvbasfawefasnfsd2354234(U(*U&'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/labsaledb?charset=utf8mb4'
# params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-MTQR317\SQLEXPRESS;DATABASE=BI;Trusted_Connection=yes;')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 8

db = SQLAlchemy(app=app)

# cloudinary.config({
#     "cloud_name": 'dxjenltg1',
#     "api_key": '279353241829545',
#     "api_secret": 'IyVAiQQyX7KjAEnnUzTVlilhb9c'
# })

# cloudinary.config(dict(cloud_name='dxjenltg1', api_key='279353241829545', api_secret='IyVAiQQyX7KjAEnnUzTVlilhb9c'))

cloudinary.config(
    cloud_name = 'dxjenltg1',
    api_key = '279353241829545',
    api_secret = 'IyVAiQQyX7KjAEnnUzTVlilhb9c'
)

login = LoginManager(app=app)
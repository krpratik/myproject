#to run pgadmin use python lib/python2.7/site-packages/pgadmin4/pgAdmin4.py

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///xyzdb'
db = SQLAlchemy(app)

# Here n is the number of devices
deviceNumbers = 2 ;

for device in range(1,deviceNumbers+1) :

  class Device(db.Model):
    __tablename__= "device"+str(device)
    id = db.Column(db.Integer, primary_key = True)
    erpm = db.Column(db.Integer)
    engine_load = db.Column(db.String(200))
    
    def __init__(self, erpm, engine_load):
      self.erpm = erpm
      self.engine_load = engine_load
      

db.create_all();


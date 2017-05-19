#to run pgadmin use python lib/python2.7/site-packages/pgadmin4/pgAdmin4.py

from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from databases import db_session
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper, clear_mappers
from databases import metadata, db_session


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///xyzdb'
# db = SQLAlchemy(app)

# Here n is the number of devices
deviceNumbers = 2 ;

class Device(object):
  query = db_session.query_property()
  # __tablename__= "device"+table_name
  # id = db.Column(db.Integer, primary_key = True)
  # erpm = db.Column(db.Integer)
  # engine_load = db.Column(db.String(200))
  def __init__(self, erpm, engine_load):
    self.erpm = erpm
    self.engine_load = engine_load
# for device in range(1,deviceNumbers+1) :
#   device_class = "device"+str(device)
#   class device_class(Device, db.Model) :
#   __tablename__="device"+str(device)


  # class Device(db.Model):
  #  __tablename__= "device"+str(device)
  #  id = db.Column(db.Integer, primary_key = True)
  #  erpm = db.Column(db.Integer)
  #  engine_load = db.Column(db.String(200))
   
  #  def __init__(self, erpm, engine_load):
  #    self.erpm = erpm
  #    self.engine_load = engine_load

# class SubClass1(BaseMixin, db.Model) :
#   pass

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
      
@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/all')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['POST'])
def new():
  if request.method == 'POST' :
    if not(request.form['erpm'] and request.form['engine_load'] and request.form['table_name']) :
      print ("Reached")
      flash('Please enter all the fields', 'error')
      return ("Empty attempt")
    else:
      erpm = request.form['erpm']
      engine_load = request.form['engine_load']
      table_name = request.form['table_name']

      devices = Table("device"+table_name, metadata,autoload= True
      )
      mapper(Device, devices)

    
      device = Device(erpm,engine_load)
      db_session.add(device)
      db_session.commit()
      clear_mappers();
      #flash('Record was successfully added')
      return ('added successfully')
  return ('Yooo')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug = True)

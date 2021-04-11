import numpy as np
import pandas as pd

import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table 
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes"""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.prcp).\
    order_by(Measurement.date).all()
    
    session.close()
    
    all_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prpc'] = prcp
        all_prcp.append(prcp_dict)
        
    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    results2 = session.query(Station.name).all()
    session.close()
    
    stations = []
    for name in results2:
        stations_dict = {}
        stations_dict['station'] = name
        stations.append(stations_dict)
    
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results3 = session.query(Measurement.date, Measurement.tobs).\
                        filter(Measurement.station == 'USC00519281').\
                        filter(Measurement.date > '2016-08-17').all()
    session.close()
    
    
    all_temps = []
    
    for date, temps in results3:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['temps'] = temps
        all_temps.append(tobs_dict)
        
    return jsonify(all_temps)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None , end=None):
    session = Session(engine)
    if not end:
        results4 = session.query()
    
    results4 = session.query()


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    


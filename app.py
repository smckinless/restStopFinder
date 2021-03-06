from flask import Flask, render_template, request, url_for
from parser import *
import os, urllib2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/restStopFinder", methods=["GET", "POST"])
def finder():

    return render_template('finder.html')

@app.route('/result', methods=["GET", "POST"])
def find_stop():
    beginLat = float(request.json['beginLat'])
    beginLon = float(request.json['beginLon'])
    endLat = float(request.json['endLat'])
    endLon = float(request.json['endLon'])
    northBound = False
    eastBound = False
    
    # checks if heading northbound
    if (endLat > beginLat):
        northBound = True

    # checks if heading eastbound
    if (endLon < beginLon):
        eastBound = True
    stop = findPosition(endLat, endLon, northBound, eastBound)
    
    # if no stop in current direction, check again
    if stop is False:
        stop = findPosition(endLat, endLon, northBound, eastBound)


    return '<iframe width="100%" height="100%" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?origin='+str(endLat)+','+str(endLon)+'&destination='+str(stop.location[1])+','+str(stop.location[0])+'&key='+YOUR_API_KEY+'" allowfullscreen></iframe>'


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)

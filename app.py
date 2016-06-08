from flask import Flask, render_template, request, url_for
from parser import *
import os, urllib2

app = Flask(__name__)
YOUR_API_KEY = ""

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/restStopFinder", methods=["GET", "POST"])
def finder():

	return render_template('finder.html')

@app.route('/result', methods=["GET", "POST"])
def find_stop():
    lat = float(request.json['lat'])
    lon = float(request.json['lon'])
    
    stop = findPosition(lat, lon)
    
    # directions = json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin="+str(lat)+","+str(lon)+"&destination="+str(stop.location[1])+","+str(stop.location[0])+"&key="))
    # steps = directions['routes'][0]['legs'][0]['steps']
    # total_distance = directions['routes'][0]['legs'][0]['distance']['text']
    # instructions = stop.name + "<br><br>You are " + total_distance + " from your destination.<br><br>"
    # for step in steps:
    #     instructions += step['html_instructions'] + " for " + step['distance']['text'] + "." + "<br>"
    return '<iframe width="100%" height="100%" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?origin='+str(lat)+','+str(lon)+'&destination='+str(stop.location[1])+','+str(stop.location[0])+'&key='+YOUR_API_KEY+'" allowfullscreen></iframe>'
    

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=False, host='0.0.0.0', port=port)

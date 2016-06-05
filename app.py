from flask import Flask, render_template, request, url_for
from parser import *
import os, urllib2

app = Flask(__name__)
YOUR_API_KEY = "AIzaSyAveMfGooZzTbOq5rVO-OeyyUbVnn6Nc3g"

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/restStopFinder", methods=["GET", "POST"])
def finder():

	return render_template('finder.html')

@app.route('/result', methods=["GET", "POST"])
def find_stop():
    print request.json
    lat = float(request.json['lat'])
    lon = float(request.json['lon'])
    #print lat
    #geocodedLocation = json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(lon)+"&key="+YOUR_API_KEY))
    #address = geocodedLocation['results'][0]['formatted_address']
    stop = findPosition(lat, lon)
    
    #stopLocation = json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(stop.location[1])+","+str(stop.location[0])+"&key="+YOUR_API_KEY))
    #stopAddress = stopLocation['results'][0]['formatted_address']
    #direction_string = '"?key="'+YOUR_API_KEY+'&origin='+address+'&destination='+stopAddress+'"'
    directions = json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin="+str(lat)+","+str(lon)+"&destination="+str(stop.location[1])+","+str(stop.location[0])+"&key="))
    #for direction in directions:
    steps = directions['routes'][0]['legs'][0]['steps']
    total_distance = directions['routes'][0]['legs'][0]['distance']['text']
    instructions = stop.name + "<br><br>You are " + total_distance + " from your destination.<br><br>"
    for step in steps:
        instructions += step['html_instructions'] + " for " + step['distance']['text'] + "." + "<br>"
    return '<iframe width="100%" height="100%" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?origin='+str(lat)+','+str(lon)+'&destination='+str(stop.location[1])+','+str(stop.location[0])+'&key='+YOUR_API_KEY+'" allowfullscreen></iframe>'
    #return "<a href=https://www.google.com/maps/embed/v1/directions?key="+YOUR_API_KEY+"&origin="+str(lat)+","+str(lon)+"&destination="+str(stop.location[1])+","+str(stop.location[0])+">Link</a>"
    #return instructions
    #render_template("result.html", steps=steps)
    #print stopAddress
    #return render_template("result.html", text=text)
    #return stop.name

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=False, host='0.0.0.0', port=port)

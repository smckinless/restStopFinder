import csv, math
from RestStop import *
from urllib2 import urlopen
from contextlib import closing
import json

def findPosition(lat, lon, northBound, eastBound):


	restStops = []


	with open('RestAreas.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			location = []
			location.append(row[0])
			location.append(row[1])
			restStops.append(RestStop(row[2], location))

	dist = 1000
	correctStop = location[0]
	for stop in restStops:
		#print stop.location
		stopLong = float(stop.location[0])
		stopLat = float(stop.location[1])
		latDistance = abs(stopLat - lat)
		longDistance = abs(stopLong - lon)
		totalDistance = math.sqrt((latDistance * latDistance) + (longDistance * longDistance))
		if northBound is True:
			if totalDistance < dist and stopLat > lat:
				dist = totalDistance
				correctStop = stop
		else:
			if totalDistance < dist and stopLat < lat:
				dist = totalDistance
				correctStop = stop
				
		if eastBound is True:
			if totalDistance < dist and stopLon < lat:
				dist = totalDistance
				correctStop = stop
		else:
			if totalDistance < dist and stopLat > lat:
				dist = totalDistance
				correctStop = stop

	return correctStop
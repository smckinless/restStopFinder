import csv, math
from RestStop import *
from urllib2 import urlopen
from contextlib import closing
import json

# finds closest rest stop to current position based on direction
def findPosition(lat, lon, northBound, eastBound):
	restStops = []

	# creates a list of rest stops in the country
	with open('RestAreas.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			location = []
			location.append(row[0])
			location.append(row[1])
			restStops.append(RestStop(row[2], location))

	dist = 1000
	correctStop = False


	for stop in restStops:
		#print stop.location
		stopLong = float(stop.location[0])
		stopLat = float(stop.location[1])
		latDistance = abs(stopLat - lat)
		longDistance = abs(stopLong - lon)
		totalDistance = math.sqrt((latDistance * latDistance) + (longDistance * longDistance))

		# checks if moving northeast
		if northBound is True and eastBound is True:
			if totalDistance < dist and stopLat > lat and stopLong > lon:
				dist = totalDistance
				foundStop = stop
				correctStop = True

		# checks if moving east and south
		elif northBound is False and eastBound is True:
			if totalDistance < dist and stopLat < lat and stopLong > lon:
				dist = totalDistance
				foundStop = stop
				correctStop = True

		# checks if moving north and west
		elif northBound is True and eastBound is False:
			if totalDistance < dist and stopLat > lat and stopLong < lon:
				dist = totalDistance
				foundStop = stop
				correctStop = True

		# moving south and west
		else:
			if totalDistance < dist and stopLat < lat and stopLong < lon:
				dist = totalDistance
				foundStop = stop
				correctStop = True


	dist = 1000

	# if no stop in current direction find nearest stop in all directions
	if correctStop is False:
		for stop in restStops:
		#print stop.location
			stopLong = float(stop.location[0])
			stopLat = float(stop.location[1])
			latDistance = abs(stopLat - lat)
			longDistance = abs(stopLong - lon)
			totalDistance = math.sqrt((latDistance * latDistance) + (longDistance * longDistance))
			if totalDistance < dist:
				dist = totalDistance
				correctStop = stop

	return correctStop
from flask import Flask, render_template, request, url_for
from parser import *
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

	return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])
def find_stop():
    print request.json
    lat = float(request.json['lat'])
    lon = float(request.json['lon'])
    
    stop = findPosition(lat, lon)
    return stop.name

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)

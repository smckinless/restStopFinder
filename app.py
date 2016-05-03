from flask import Flask, render_template
from parser import *
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	stop = findPosition()
	return stop.name

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

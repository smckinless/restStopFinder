from flask import Flask, render_template
from parser import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	stop = findPosition()
	return stop.name

if __name__ == '__main__':
	app.run()

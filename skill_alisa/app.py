from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=['GET','POST'])
def main():
	logging.info(request.json)


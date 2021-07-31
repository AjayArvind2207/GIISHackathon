import time

import firebase_admin
import json
import requests
from firebase_admin import firestore
from flask import Flask, jsonify, render_template, request, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
CORS(app)

cred_obj = firebase_admin.credentials.Certificate(
    'quarantine-plus-plus-firebase-adminsdk-qpwi2-77a48fc6ca.json')
default_app = firebase_admin.initialize_app(cred_obj)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/temp")
def temperature():
    return render_template("temp.html")

@app.route("/entertainment")
def entertainment():
    return render_template('entertainment.html')

@app.route("/upcoming")
def upcoming():
    return render_template('upcoming.html')


@app.route("/temperature", methods = ['POST'])
def get_temperature():
    temp = request.form["temperature"]
    # or however login works
    user = request.form["user"]

    db = firestore.client()
    doc_ref = db.collection(u'temperatures').document()
    data = {
        u'name': user,
        u'temp': temp,
        u'time': time.time()
    }
    doc_ref.set(data)

    return jsonify({'id': doc_ref.id, 'time': time.time()})


@app.route('/weather', methods = ['GET'])
def weather() -> None:
    '''This fetches the weather data'''
    api_key = 'a6280859274843c64f27cccd1059ba8b'
    city_id = '1880252'
    url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'
    data = requests.get(url).text
    return jsonify(json.loads(data))

@app.route('/guten/<search>', methods = ['GET'])
def guten(search):
    url = f'https://gutendex.com/books/?search={search}'
    data = requests.get(url).text
    
    return jsonify(json.loads(data))


@app.route("/emergency", methods = ['POST', 'GET'])
def emergency():
    # or however login works
    user = request.form["user"]

    db = firestore.client()
    doc_ref = db.collection(u'emergency').document()
    data = {
        u'name': user,
        u'time': time.time()
    }
    doc_ref.set(data)
    
    return jsonify({'id': doc_ref.id, 'time': time.time()})



if __name__ == "__main__":
    app.run(debug=True)

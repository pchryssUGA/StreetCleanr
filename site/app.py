import tensorflow as tf
import os
import cv2
import imghdr
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
from tensorflow.keras.models import load_model
'''
import os
import requests
from flask import Flask, redirect, url_for, render_template, request, session
from flask_dropzone import Dropzone
from dotenv import load_dotenv
#from db import db
#from flask_migrate import Migrate
from test import test_blueprint
import random
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask('__main__', static_folder='static', template_folder='templates')
app.register_blueprint(test_blueprint, url_prefix='/test')
app.config.update(UPLOADED_PATH = os.path.join(basedir, 'static/uploads'),
                  DROPZONE_MAX_FILE_SIZE = 1024,
                  DROPZONE_TIMEOUT = 5*60*1000,
                  DROPZONE_MAX_FILES=20,
                  DROPZONE_REDIRECT_VIEW='test.result')
dropzone = Dropzone(app)

cars = ['static/images/cars/car1.jpg',
        'static/images/cars/car2.jpg',
        'static/images/cars/car3.jpg',
        'static/images/cars/car4.jpg',
        'static/images/cars/car5.jpg',
        'static/images/cars/car6.jpg']

places = ['Tate Student Center, Baxter Street, Athens, GA, US',
          'Joe Frank Harris Commons, Athens, GA, USA',
          'Boyd Graduate Studies Research Center, D. W. Brooks Drive, Athens, GA, USA,',
          'The Niche Dining Commons, Athens, GA, USA',
          'UGA Arch, U.S. 78 Business, Athens, GA, USA']

#Home page
@app.route('/', methods={'POST','GET'})
def home():
    return render_template('index.html')

#Rewards page
@app.route('/rewards', methods={'POST','GET'})
def rewards():
    return render_template('rewards.html')

#Training page
@app.route('/train', methods={'POST','GET'})
def train():
    this_dir = os.path.join('static','testing')
    if len(os.listdir(os.path.join('site',this_dir,'new'))) == 0:
        return render_template('blank.html')
    
    if request.method == 'POST':
        img_type = request.form['type']
        img_url = request.form['url']
        img_name = img_url.split('/')[-1]
        #dest = os.path.join('site',this_dir, img_type, img_name)
        dest_path = os.path.join('site', this_dir, img_type, img_name)
        img_path = os.path.join('site', img_url)
        os.rename(img_path, dest_path)
    ran = random.choice(os.listdir(os.path.join('site',this_dir,'new')))
    img_url = os.path.join(this_dir,'new',ran)
    return render_template('train.html',values=[img_url])

@app.route('/route', methods={'POST','GET'})
def route():
    return render_template('route.html')

@app.route('/map', methods={'POST','GET'})
def map():
    if request.method == 'POST':
        location = request.form['location']
    return render_template('map.html', values=[location, places])

if __name__ == '__main__':
    app.run(debug=True)
'''


    












import os
import requests
from flask import Flask, redirect, url_for, render_template, request, session
from flask_dropzone import Dropzone
from dotenv import load_dotenv
#from db import db
#from flask_migrate import Migrate
from test import test_blueprint
import random
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask('__main__', static_folder='static', template_folder='templates')
app.register_blueprint(test_blueprint, url_prefix='/test')
app.config.update(UPLOADED_PATH = os.path.join(basedir, 'static/images'),
                  DROPZONE_MAX_FILE_SIZE = 1024,
                  DROPZONE_TIMEOUT = 5*60*1000,
                  DROPZONE_MAX_FILES=20,
                  DROPZONE_REDIRECT_VIEW='test.result')
dropzone = Dropzone(app)

cars = ['static/images/cars/car1.jpg',
        'static/images/cars/car2.jpg',
        'static/images/cars/car3.jpg',
        'static/images/cars/car4.jpg',
        'static/images/cars/car5.jpg',
        'static/images/cars/car6.jpg']

#Home page
@app.route('/', methods={'POST','GET'})
def home():
    return render_template('index.html')

#Upload page
@app.route('/upload', methods={'POST','GET'})
def upload():
    return render_template('upload.html')

#Rewards page
@app.route('/rewards', methods={'POST','GET'})
def rewards():
    return render_template('rewards.html')

#Training page
@app.route('/train', methods={'POST','GET'})
def train():
    this_dir = os.path.join('static','testing')
    if len(os.listdir(os.path.join('site',this_dir,'new'))) == 0:
        return render_template('blank.html')
    
    if request.method == 'POST':
        img_type = request.form['type']
        img_url = request.form['url']
        img_name = img_url.split('/')[-1]
        #dest = os.path.join('site',this_dir, img_type, img_name)
        dest_path = os.path.join('site', this_dir, img_type, img_name)
        img_path = os.path.join('site', img_url)
        os.rename(img_path, dest_path)
    ran = random.choice(os.listdir(os.path.join('site',this_dir,'new')))
    img_url = os.path.join(this_dir,'new',ran)
    return render_template('train.html',values=[img_url])

@app.route('/route', methods={'POST','GET'})
def route():
    return render_template('route.html')

@app.route('/map', methods={'POST','GET'})
def map():
    if request.method == 'POST':
        waypoints = [request.form['trash1'],
                 request.form['trash2'],
                 request.form['trash3'],
                 request.form['trash4'],
                 request.form['trash5']] 
        MAP_API = 'https://maps.googleapis.com/maps/api/geocode/json?'
        KEY = 'AIzaSyBL2hXd1GhFewItloD4CFiVRwKG50hX-_0'
        location = request.form['location']
        location.encode(encoding='UTF-8')
        response = requests.get(MAP_API+'address='+location+'&key='+KEY)
        json = response.json()['results'][0]['geometry']['location']
        lat = str(json['lat'])
        lng = str(json['lng'])
        for i in range(len(waypoints)):
            curr = waypoints[i]
            curr.encode(encoding='UTF-8')
            response = requests.get(MAP_API+'address='+curr+'&key='+KEY)
            json = response.json()['results'][0]['geometry']['location']
            waypoints[i] = ''+str(json['lat'])+','+str(json['lng'])
    return render_template('map.html', values=[lat,lng,waypoints[0], waypoints[1],waypoints[2],waypoints[3],waypoints[4]])

if __name__ == '__main__':
    app.run(debug=True)
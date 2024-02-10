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

#Training page
@app.route('/train', methods={'POST','GET'})
def train():
    url = cars[0]
    if request.method == 'POST':
        url = cars[random.randint(0,len(cars)-1)]
    return render_template('train.html', values=[url])

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
from flask import Flask, Blueprint, render_template, request, redirect, url_for, current_app
from flask_dropzone import Dropzone
#from db import db
#from flask_sqlachemy import
import requests
import os
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
from dotenv import load_dotenv
load_dotenv()

test_blueprint = Blueprint('test', __name__, static_folder='static', template_folder='templates_test')

filename = None
str = ''
classify = ''

@test_blueprint.route('/', methods=['POST','GET'])
def test():
    if request.method == 'POST':
        if request.form['new'] == 'new':
            file=request.form['file']
            os.remove(os.path.join('site/'+file))
    return render_template('test.html', values='blank')
    
@test_blueprint.route('/result', methods=['POST','GET'])
def result():
    global filename
    global str
    global classify
    yhat = ''
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(current_app.config['UPLOADED_PATH'],f.filename))
        print()
        print()
        print(os.path.join(current_app.config['UPLOADED_PATH'],f.filename))
        img = cv2.imread(os.path.join('site','static','images',f.filename))
        resize = tf.image.resize(img, (256, 256))
        new_model = load_model(os.path.join('site','models', 'streetsmodel.h5'))
        yhatnew = new_model.predict(np.expand_dims(resize/255, 0))
        print(yhatnew)
        if yhatnew > 0.5:
            classify = 'dirty'
        else:
            classify = 'clean'

        filename = f.filename
        str = 'static/images/'+filename
    return render_template('result.html', values=[str, classify])

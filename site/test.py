from flask import Flask, Blueprint, render_template, request, redirect, url_for, current_app
from flask_dropzone import Dropzone
#from db import db
#from flask_sqlachemy import
import requests
import os
from dotenv import load_dotenv
load_dotenv()

test_blueprint = Blueprint('test', __name__, static_folder='static', template_folder='templates_test')

filename = None

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
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(current_app.config['UPLOADED_PATH'],f.filename))
        filename = f.filename
    else:
        return render_template('result.html', values=['clean','static/uploads/'+filename])

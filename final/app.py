#!flask/bin/python

import sys
import json
from flask import Flask, render_template, request
from img_utils_demo import demo
from img_utils import mls_rigid_deformation, mls_rigid_deformation_inv

app = Flask(__name__)

@app.route('/')
def output():
    return render_template('index.html')

@app.route('/show', methods = ['POST'])
def worker():
    data = request.get_json(force=True)
    print(data)
    demo(mls_rigid_deformation, mls_rigid_deformation_inv, "Rigid", data)
    return 'done!'

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run()

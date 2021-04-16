# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:09:06 2021

@author: MYPC
"""

 from flask import Flask
app = Flask(__name__)
@app.route('/') #app.route(rule,options)
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run() # local host web browser
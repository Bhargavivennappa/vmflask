# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:54:44 2021

@author: MYPC
"""

from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/hello/<name>')
def hello_world(name):
    return "hello %s" %name
@app.route('/user/<user>')
def user(user):
    return "hello user %s" %user
@app.route('/value/<int:value>')
def value(value):
    return "the value is %d" %value



if __name__ == '__main__':
    app.run(debug=True)
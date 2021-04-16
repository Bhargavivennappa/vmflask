# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:54:33 2021

@author: MYPC
"""

from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/admin')
def hello_admin():
    return "hello admin"
@app.route('/guest/<guest>')
def hello_guest(guest):
    return "hello %s guest"%guest
@app.route('/user/<name>')
def hello_user():
    if (name=='admin'):
        return redirect(url_for("hello_admin"))
    else:
        return redirecr(url_for('hello_guest',guest=name))




if __name__ == '__main__':
    app.run(debug=True)
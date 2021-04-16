# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:56:31 2021

@author: MYPC
"""

from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/sigin',methods=["POST"])
def login() :
    if request.method=="POST":
        user=request.form["name"] 
        mail=request.form["mail"] 
        qual=request.form["qual"]
        age=request.form["age"]
        return render_template("login.html",x=user,y=mail,z=qual,v=age)
if(__name__=='__main__'):
    app.run(debug=True)

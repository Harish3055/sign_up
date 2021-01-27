# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:02:04 2020

@author: Harish
"""

def number(di):
    for i in di:
        if ord(i)>=48 and ord(i)<=57:
            return(1)
    return(0)
def large(di):
    for i in di:
        if ord(i)>=65 and ord(i)<=91:
            return(1)
    return(0)
def small(di):
    for i in di:
        if ord(i)>=97 and ord(i)<=122:
            return(1)
    return(0)
def special(di):
    lis=[ord('!'),ord('@'),ord('#'),ord('$'),ord('%'),ord('^'),ord('&'),ord('*'),ord('?'),ord('~')]
    for i in di:
        if ord(i) in lis:
            return(1)
    return(0)    
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database="login"
)

mycursor = mydb.cursor()
import flask
from flask import Flask, request, render_template,redirect
from flask import current_app, url_for
app = Flask(__name__)
@app.route('/<name>')
def home(name):
    if name=='log':
        return render_template('index0.html')
    else :
        return render_template('signup.html')
@app.route('/log',methods=['POST'])
def login():
    ws=request.form['user_name']#username name
    di=request.form['password']#password
    #ws=request.form['user_name']#username name
    #di=request.form['password']#password
    query1 = "SELECT user_name FROM user2"
    ## getting records from the table
    mycursor.execute(query1)    
    ## fetching all records from the 'cursor' object
    records1 = mycursor.fetchall()
    query2 ="SELECT password FROM user2"
    mycursor.execute(query2)
    records2 = mycursor.fetchall()
    records2 = list(sum(records2, ()))
    records1 = list(sum(records1, ()))
    if ws in records1 and di in records2:#if password is correct it redirects the calculator page
        print(ws)
        print(di)    
        return redirect('http://127.0.0.1:5500/index.html')    
    else:
        return render_template('index0.html',failed='Enter Correct Password :)')  #if not it says Enter correct password   
@app.route('/sign',methods=['POST'])
def signup():
    ws=request.form['user_name']#username name
    di=request.form['password']#password
    ch=request.form['Check']  
    query1 = "SELECT user_name FROM user2"
    mycursor.execute(query1)
    records1 = mycursor.fetchall()
    query2 ="SELECT password FROM user2"
    mycursor.execute(query2)
    records2 = mycursor.fetchall()
    records2 = list(sum(records2, ()))
    records1 = list(sum(records1, ()))
    
    if ch=='on' and ws not in records1 and di not in records2 and len(di)>=6 and number(di)==1 and special(di)==1 and large(di)==1 and small(di)==1:
         sql = "INSERT INTO user2 (user_name, password) VALUES (%s ,%s)"
         val = (ws,di)
         print(len(di)>=6, number(di)==1 , special(di)==1 , large(di)==1, small(di)==1)
         mycursor.execute(sql, val)
         mydb.commit()
         return redirect('http://192.168.43.29:3055/log')
    elif ch=='on' and ws not in records1 and di not in records2  and len(di)<6 or number(di)==0 or special(di)==0 or large(di)==0 or small(di)==0:
        return render_template('signup.html',failed='password must contain numbers,lower,uppper,special characters :)')  #if not it says Enter correct password
    elif ch=='on' and ws in records1 and di in records2 or ws in records1 and di not in records2 or ws not in records1 and di in records2:
        return render_template('signup.html',failed='Credential already exist :)')  #if not it says Enter correct password
#@pp.route('login/')    
if __name__ == "__main__":
    app.run(host='192.168.43.29',port=3055)    
    

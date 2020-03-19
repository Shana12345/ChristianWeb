from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import os
import urllib3

app = Flask(__name__) #assign your name 'app'
app.config["MYSQL_HOST"] = os.environ['MYSQL'] #IP address of SQL database 
app.config["MYSQL_USER"] = os.environ['MYSQLUSER']#Username for DB
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASSWORD']#Password for DB
app.config["MYSQL_DB"] = os.environ['MYSQLDB'] #Databse being used
app.config['SECRET_KEY'] = 'secret'

mysql = MySQL(app) # What to define 'MySQL' as 'mysql'



def test_url():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/')
    assert 200 == r.status


def test_url_About():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/About')
    assert 200 == r.status


def test_url_CreateandRecieve():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/CreateandRecieve')
    assert 200 == r.status

def test_url_EnterQuote():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/EnterQuote')
    assert 200 == r.status

def test_url_DeTrata():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/De%20que%20se%20trata')
    assert 200 == r.status

def test_select():
    with app.app_context():
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM CUSTOMER_QUOTE")
        mysql.connection.commit()
        cur.close()
    print(resultValue)
    assert 2 == resultValue


def test_insert():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO CUSTOMER_QUOTE (NICK_NAME, QUOTE, FAVORITE_AUTHOR)  VALUES ('@sHHH', 'Have faith', 4)")
        mysql.connection.commit()
        cur.execute("SELECT * FROM CUSTOMER_QUOTE") #this gets record after update
        record_after = cur.fetchall()
        print(record_after)
        m=[]
        for i in record_after:
            for j in i:
                m.append(j)
        cur.close()
    print(m)
    # lena = len(record_after)
    assert('@sHHH') == m[-3]
    assert('Have faith') == m[-2]
    assert(4) == m[-1]
   

def test_update():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE CUSTOMER_QUOTE SET QUOTE = 'hola' WHERE NICK_NAME  = '@sHHH'")
        mysql.connection.commit()
        cur.execute("SELECT * FROM CUSTOMER_QUOTE")
        records_after = cur.fetchall()
        l=[]
        for d in records_after:
            for o in d:
                l.append(o)
        cur.close()
    lena = len(records_after)
    assert('hola') == l[-2]

def test_delete():
    with app.app_context():
        cur = mysql.connection.cursor()
        records_before = cur.execute("SELECT * FROM CUSTOMER_QUOTE")
        print(records_before)
        mysql.connection.commit()
        cur.execute("DELETE FROM CUSTOMER_QUOTE WHERE NICK_NAME = '@sHHH'")
        mysql.connection.commit()
        records_after = cur.execute("SELECT * FROM CUSTOMER_QUOTE")
        print(records_after)
        mysql.connection.commit()
        cur.close()
    assert records_before - 1 == records_after
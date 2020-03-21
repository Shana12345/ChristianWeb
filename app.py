from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import os


app = Flask(__name__) #assign your name 'app'
app.config["MYSQL_HOST"] = os.environ['MYSQLHOST'] #IP address of SQL database 
app.config["MYSQL_USER"] = os.environ['MYSQLUSER']#Username for DB
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASSWORD']#Password for DB
app.config["MYSQL_DB"] = os.environ['MYSQLDB'] #Databse being used
app.config['SECRET_KEY'] = 'secret'

mysql = MySQL(app) # What to define 'MySQL' as 'mysql'

@app.route('/')
def Main():
    cur = mysql.connection.cursor()
    cur.execute("SELECT c.NICK_NAME, c.QUOTE, a.AUTHOR, a.AUTHOR_QUOTE FROM CUSTOMER_QUOTE c INNER JOIN AUTHOR a ON (c.FAVORITE_AUTHOR=a.AID)")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    info = []
    for row in rows:
        info.append(row)
    return render_template('Home.html',  title='Light', info1=info)


   
@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/De que se trata')
def Espanol():
    return render_template('De que se trata.html', title='Jesus es la manera y la luz')

@app.route('/CreateandRecieve', methods = ['GET', 'POST'])
def CreateandRecieve():
    if request.method == 'POST':
        # flash("Submitted Sucessfully!", 'success')
        userDetails=request.form
        if userDetails['password'] != userDetails['comfirmpass']:
            flash("Password either didn't match or you already have an account, please login", 'danger')
        # return render_template('CreateandReceive.html')
        print(userDetails)
        name = userDetails['name']
        surname = userDetails['surname']
        password=userDetails['password']
        email=userDetails['email']
        comfirmpass=userDetails['comfirmpass']
        futureAuthors=userDetails['futureAuthors']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (name, surname, password, email, comfirmpass, futureAuthors) VALUES(%s, %s, %s, %s,%s,%s)", (name, surname, password, email, comfirmpass, futureAuthors))
        mysql.connection.commit()
        cur.close()
        return redirect('/Cr')
    return render_template('CreateandRecieve.html')

@app.route('/Cr')
def fa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT futureAuthors FROM user")
    mysql.connection.commit()
    rowws = cur.fetchall()
    cur.close()
    infoo = []
    for ro in rowws:
        infoo.append(ro)
    return render_template('CreateandRecieve.html', info2=infoo)
    

    
@app.route('/EnterQuote', methods = ['GET', 'POST'])
def customerQuotes():
        
    if request.method == 'POST':
        userQuotes=request.form
        NICK_NAME=userQuotes['NICK_NAME']
        QUOTE=userQuotes['QUOTE']
        FAVORITE_AUTHOR=userQuotes['FAVORITE_AUTHOR']
        # print(quotes)
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT NICK_NAME FROM CUSTOMER_QUOTE WHERE NICK_NAME = (%s)", [NICK_NAME])
        if resultValue > 0:
            flash("Nickname already exists, quote not submitted", 'danger')
        else:
            flash("submitted sucessfully", 'success')
            cur.execute("INSERT INTO CUSTOMER_QUOTE (NICK_NAME, QUOTE, FAVORITE_AUTHOR) VALUES(%s, %s, %s)", [NICK_NAME, QUOTE, FAVORITE_AUTHOR])
            mysql.connection.commit()  
            cur.close()
            return redirect('/')
    return render_template('EnterQuote.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        NICK_NAME = request.form['NICK_NAME']
        QUOTE = request.form['QUOTE']
        FAVORITE_AUTHOR = request.form['FAVORITE_AUTHOR']
        cur.execute("UPDATE CUSTOMER_QUOTE SET QUOTE = %s, FAVORITE_AUTHOR = %s WHERE NICK_NAME= %s", (QUOTE, FAVORITE_AUTHOR, NICK_NAME))
        mysql.connection.commit()
        cur.close()
        flash('Updated successfully', 'success')
        return redirect('/')
    return render_template('EnterQuote.html')

@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        NICK_NAME = request.form['NICK_NAME']
        cur.execute("DELETE FROM CUSTOMER_QUOTE WHERE NICK_NAME = %s", [NICK_NAME])
        mysql.connection.commit()
        cur.close()
        flash('Entry successfully deleted', 'success')
        return redirect('/')
    return render_template('EnterQuote.html')


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)



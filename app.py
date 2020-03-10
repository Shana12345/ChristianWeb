from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import os

app = Flask(__name__) #assign your name 'app'
app.secret_key = "flash message"
app.config["MYSQL_HOST"] = os.environ['MYSQL'] #IP address of SQL database 
app.config["MYSQL_USER"] = os.environ['MYSQLUSER']#Username for DB
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASSWORD']#Password for DB
app.config["MYSQL_DB"] = os.environ['MYSQLDB'] #Databse being used

mysql = MySQL(app) # What to define 'MySQL' as 'mysql'


@app.route('/')
def Main():
    return render_template('Home.html', title='Light')
   
@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/De que se trata')
def Espanol():
    return render_template('De que se trata.html', title='Jesus es la manera y la luz')

@app.route('/CreateandRecieve', methods = ['GET', 'POST'])
def CreateandRecieve():
    if request.method == 'POST':
        flash("Submitted Sucessfully!")
        userDetails=request.form
        if userDetails['passwd'] != userDetails['comfirmpass']:
            flash("Password either didn't match or you aalready have an account")
            return render_template('CreateandReceive.html')
        print(userDetails)
        name = userDetails['name']
        surname = userDetails['surname']
        email=userDetails['email']
        password=userDetails['passwd']
        comfirmpass=userDetails['comfirmpass']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (name, surname, password, email, comfirmpass) VALUES(%s, %s, %s, %s,%s)", (name, surname, password, email, comfirmpass))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Main'), 'Submitted sucessfully')
    return render_template('CreateandRecieve.html')
    

    
@app.route('/EnterQuote', methods = ['GET', 'POST'])
def customerQuote():
    if request.method == 'POST':
        userQuotes=request.form
        quotes=userQuotes['quotes']
        print(quotes)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customerQuotes (quotes) VALUES(%s)", [quotes])
        mysql.connection.commit()
        cur.close()
    return render_template('EnterQuote.html')




   




# for i in password:
#     output=''
#     for x in range(i):
#         output += '*'
#         print(output)

# return 'Submitted sucessfully'
    # return redirect(url_for('home'))

# @app.route('/Make and Recieve Devotional')
# def Makemehappy():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT customer_quote FROM quotes WHERE u_id = customerInfo')
#     mysql.connection.commit()
#     rows = cur.fetchall()
#     cur.close()
    
    
# customerInfo = []
# for i in rows:
#     customerInfo.append(i)

#     # print(info)
#     return render_template('CreateandRecieve.html', details = customerInfo)

# @app.route('/account/delete')
# def account_delete():
#     cur 

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)



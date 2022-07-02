from flask import Flask, render_template, request #Import flask using pip
from flask_mysqldb import MySQL  #Import flask_mysqldb

app = Flask(__name__)

# Required
app.config['MYSQL_HOST'] = 'localhost'  #Your sql host name
app.config['MYSQL_USER'] = 'root'       #Your sql user name
app.config['MYSQL_PASSWORD'] = 'Ethanshine#123' # Your password
app.config['MYSQL_DB'] = 'test' # Your database name
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('index.html') #Your html code

@app.route("/register", methods = ['POST', 'GET'])
def register():
    firstname = request.form.get("firstname");
    lastname = request.form.get("lastname");
    email = request.form.get('email');
    password = request.form.get('password');
    gender = request.form.get('gender');
    number = request.form.get('number');
    cur = mysql.connection.cursor() # mysql connection
    cur.execute("INSERT INTO test.registration (firstname, lastname,gender,email,password,number) VALUES (%s, %s, %s, %s, %s,%s)",
              (firstname, lastname,gender,email,password,number))#Inserting table contents
                                                                 # Id is not given because it is defined as auto incrementing

    mysql.connection.commit()
    cur.close()
    #mysql.commit()  # apply change
    return render_template("createThanks.html")    #Registered Successfully html is written in createThanks.html

if __name__ == "__main__":
    app.run(debug=True)

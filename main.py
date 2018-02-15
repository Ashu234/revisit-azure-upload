from flask import Flask, render_template, request, redirect, url_for, session
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
import mysql.connector
from mysql.connector import errorcode
import os

app = Flask(__name__)

config = {
  'host':'myserver-mysql-ashu.mysql.database.azure.com',
  'user':'root123@myserver-mysql-ashu',
  'password':'Superman123',
  'database':'mysqlashudb',
  'ssl_ca':'BaltimoreCyberTrustRoot.crt.pem'
}


@app.route('/')
def index():
  session['logged_in'] = True
  try:
     conn = mysql.connector.connect(**config)
     print("Connection established")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    username = 'ashutosh'
    title = 'maccafee'
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (username, title) VALUES (%s, %s);", (username, title))
    conn.commit()
    cursor.close()
    conn.close()
  return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
app.secret_key = 'secretkey'
    

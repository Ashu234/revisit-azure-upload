from flask import Flask, render_template, request, redirect, url_for, session
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
import mysql.connector
import os

app = Flask(__name__)


@app.route('/')
def index():
  session['logged_in'] = True
  return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'secretkey'
    app.run(debug=True)
    

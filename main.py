from flask import Flask, render_template, request, redirect, url_for
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
import mysql.connectora
import os

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

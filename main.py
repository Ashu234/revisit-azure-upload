from flask import Flask, render_template, request, redirect, url_for, session
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
import os

app = Flask(__name__)

block_blob_service = BlockBlobService(account_name='ashuazurestorage', account_key='HGvsHgPPFOp64gztvR6B9g+RNUUqzwhl+aNid8wpwca1uwejBMEhyVkP3oev1SKEnI5eeq4EIXWfcvzWjxAjuQ==')
block_blob_service.set_container_acl('ashu-blob-container', public_access=PublicAccess.Container)

@app.route('/')
def hello_world():
  return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        return render_template('complete.html')
    return render_template('upload.html')
  
@app.route('/rating/<string:title>/')
def rating(title):
    if request.method == 'POST':
      rating = request.form['rating']
      return redirect(url_for('complete.html', rating=rating))
    return render_template('rating.html', title=title)

  
class MyBlob(object):
    url = ''
    size = 0
    title = ''
    date = ''

    def __init__(self, url, size, title, date):
        self.url = url
        self.size = (size/1024)
        self.title = title
        self.date = date


@app.route('/viewImages', methods=['GET', 'POST'])
def viewImages():
    blobs = []
    generators = block_blob_service.list_blobs('ashu-blob-container')
    for blob in generators:
        blob_url = block_blob_service.make_blob_url('ashu-blob-container', blob.name, protocol=None, sas_token=None)
        myBlob = MyBlob(blob_url,blob.properties.content_length,blob.name,blob.properties.last_modified)
        blobs.append(myBlob)
    return render_template('viewImages.html', blobs=blobs)

if __name__ == '__main__':
  app.run()

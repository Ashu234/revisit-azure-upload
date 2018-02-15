from flask import Flask, render_template, request, redirect, url_for, session
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
import mysql.connector
from mysql.connector import errorcode
import os

app = Flask(__name__)

block_blob_service = BlockBlobService(account_name='ashuazurestorage', account_key='HGvsHgPPFOp64gztvR6B9g+RNUUqzwhl+aNid8wpwca1uwejBMEhyVkP3oev1SKEnI5eeq4EIXWfcvzWjxAjuQ==')
#block_blob_service.create_container('ashu-blob-container', public_access=PublicAccess.Container)
block_blob_service.set_container_acl('ashu-blob-container', public_access=PublicAccess.Container)

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
    #cursor.execute("INSERT INTO images (username, title) VALUES (%s, %s);", (username, title))
    result = cursor.execute("SELECT * FROM images;")
    rows = cursor.fetchall()
    return render_template('viewdata.html', rows=rows)
    cursor.close()
    conn.close()
  return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for file in request.files.getlist("file"):
            file_to_upload = file.filename
            full_path_to_file = os.path.join(os.path.dirname(__file__), file_to_upload)
            app.logger.info(file_to_upload)
            block_blob_service.create_blob_from_path(
            'ashu-blob-container',
            file_to_upload,
            full_path_to_file,
            content_settings=ContentSettings(content_type='image/png')
            )
        return render_template('complete.html')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
app.secret_key = 'secretkey'
    

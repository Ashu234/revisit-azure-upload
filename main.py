from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '''
    <!doctype html>
      <title>Upload new File</title>
      <h1>Upload new File</h1>
      <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file>
         <input type=submit value=Upload>
      </form>
    '''

if __name__ == '__main__':
  app.run()

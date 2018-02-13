from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        return render_template('complete.html')
    return render_template('upload.html')

if __name__ == '__main__':
  app.run()

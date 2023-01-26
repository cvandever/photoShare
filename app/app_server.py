#!/user/bin/python

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_bootstrap import Bootstrap5 as Bootstrap
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/app/static/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template('base.html', title='Home Page')

@app.route("/upload")
def upload_page():
    return render_template('upload.html', title='File Upload')

@app.route('/upload/accepted', methods=['GET','POST'])
def import_file():
    uploaded = []
    if request.method == "POST":
        files = request.files.getlist('file')
        for file in files:
            try:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                uploaded.append(file.filename)
            except Exception as e:
                return  render_template('error.html',e)
    return render_template('viewall.html',file=uploaded)

@app.route('/viewpictures',  methods=['GET', 'POST'])
def load_files():
    files = os.listdir('/app/static/files/')
    return render_template('viewall.html', files=files)

    
if __name__ == "__main__":
    app.run()
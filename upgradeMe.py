#!/usr/bin/python3

#
# Ce programme analyse une image integrant un code barre 
# au format pdf417, lit les donnees puis modifie la classe 
# de de economie vers business, puis regenere un code barre.
#
# Ne pas utiliser en prod \o/
#

from plane import Plane
import sys
from flask import Flask, render_template, request

def secure_filename(name):
   return name.replace(' ', '_')

app = Flask(__name__)
UPLOAD_FOLDER = '/home/victor/Perso/vic/Upgrade-Me-And-Fly/static/uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/toto')
def root_index():
   return "Hello World"

@app.route('/')
def uploaded_file():
   return render_template('upload.html', site_title="Upgrade this!")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      imagepath = './static/uploaded/' + secure_filename(f.filename)
      f.save(imagepath)
      airbus = Plane(imagepath)
      airbus.fly()
      new_image_path = airbus.get_updated_filepath()
      return render_template('end.html', picture_name=new_image_path)

if __name__ == '__main__': 
   app.run(host='0.0.0.0', debug = True) 

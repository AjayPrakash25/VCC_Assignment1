#flask application

from flask import Flask
import os 
app = Flask(__name__)

@app.route('/', methods = ['get'])

def home():
  return ("Hello welcome to VCC by G23ai2112")
if __name__== "__main__":
 app.run(debug=True,host="0.0.0.0", port = 5000)

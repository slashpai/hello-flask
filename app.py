import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

color = os.environ.get('APP_COLOR') or 'green'

@app.route('/')
def hello_flask():
  return render_template('hello.html', color = color)

if __name__ == '__main__':
    app.run()

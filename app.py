import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def add():
    page = '<html><body><h1>'
    page += '<p> Addition: '
    page += generator.addition(4,3).__str__()
    page += '</p></h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
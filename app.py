# from flask import Flask
import flask

app = flask.Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello </p>"

yes = 3

@app.route('/')
def home():
    return flask.render_template('base.html')

#py -m flask run


@app.route('/gardening')

def gardening_info():

    return flask.render_template('gardening.html')

 

@app.route('/cooking')

def cooking_details():

    return flask.render_template('cooking.html')

 

@app.route('/sci-fi')

def sci_fi_world():

       return flask.render_template('sci_fi.html')

 

if __name__ == '__main__':

       app.run(debug=True)

   
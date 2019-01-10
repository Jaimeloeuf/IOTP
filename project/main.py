"""
Description:
Code for IOTP Project

API  (Only get and post methods are allowed):
GET:
    /	or	/index -> static html file of user home page created using the Jinja templating engine
    /login -> static html returned for user to enter data and submit form data

POST:
    /login -> endpoint for posting username and password over to server for verification.

"""
# Dependencies
# Server dependencies
from flask import Flask, render_template, redirect, url_for, request, abort, jsonify
# To get environmental variables avail to the process
from os import environ
from pi_controller import buzzer

# 'Global' object for Flask server
app = Flask(__name__)

# Flask server routes

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home_page():
    # Check if the user logged in already by looking for a valid JWT.

    # If the user is not logged in
    redirect(url_for('login'))
    # Use put user data into home page and send it back
    return render_template('./index.html', name = name)

# Flask Route to mimic pressing the button
@app.route('/login', methods=['POST'])
def login():
    if request.headers.get('authorization')
        redirect(url_for('home')) # If user already logged in with valid JWT, then redirect to home page

    if 'Authorization' in request.headers:
        redirect(url_for('home')) # If user already logged in with valid JWT, then redirect to home page

    credentials = request.form
    for key, val in credentials.items():
        if key == 'username':
            usr = val
        elif key == 'password':
            passwd = val

    # Call DB to check password
    # If matches, create a JWT for the user
    checkPasswd()

# Server Route to test if remote server is online
@app.route('/ping', methods=['GET'])
def ping():
    # Default 200 status code will be sent back
    return


# For authentication usage
from passlib.hash import pbkdf2_sha256 as sha256

def generate_hash(password):
    return sha256.hash(password)

def verify_hash(password, hash):
    return sha256.verify(password, hash)



    
if __name__ == "__main__":
    # Use PORT from the environment if defined, otherwise default to 5000.
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
# -*- coding: utf-8 -*
# Librarys he
#from OpenSSL import SSL -- Commented Due To Using Different SSL --
import requests
import threading
from requests import get
from flask_api import status
from twilio.rest import Client
from flask_talisman import Talisman
from flask import Flask, render_template, redirect,url_for, request, Blueprint


# Variables
app = Flask(__name__)
#context = ('certificate.crt', 'private.key') -- Commented Due To Using Different SSL --
#sslify = SSLify(app) -- Commented Due To Using Different SSL --

# Settings
Talisman(app) # Force HTTPS
app.config['SECRET_KEY'] = b'\xd5\x01|\xa5U\x17\xc4\x7f\xc6E\xb55\xbe\x17N\x14\xd1\xd8\xb9\x7f+\x8a\x14\x1d'

#Functions
def post(page, method, ip):
	url = "http://argon.zade.ngrok.io/submit"
	post_data = {'text': 'hi'}
	x = requests.post(url, data = post_data)
	account_sid = 'i dont really want to put this on codeshare'
	auth_token = 'i dont really want to put this on codeshare'
	client = Client(account_sid, auth_token)
	message = client.messages.create(
								 from_='whatsapp:+14155238886',
								 body='[{}] Someone Viewed The Page: {} From The IP: {}'.format(method, page, ip),
								 status_callback='https://postb.in/1600454235088-5335026269312',
								 to='whatsapp:+447765183203'
						  )

def before(page, method, ip):
	sprint = threading.Thread(target=post, args = (page, method, ip))
	sprint.start()

# Routes
@app.route('/')
def index():
# 	before("home", request.method, request.remote_addr)
	return render_template("coming-soon.html"), 503 #Coming Soon


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.errorhandler(404)
def not_found(e):
# 	before("404-FORWARDER", request.method, request.remote_addr)
	return render_template("404.html"), 404

@app.route('/404')
def error():
# 	before("404", request.method, request.remote_addr)
	return render_template("404.html")

@app.route('/test')
def name():
# 	before("test", request.method, request.remote_addr)
	return "Hi Dad!"

@app.route('/email-gen')
def email_gen():
# 	before("email-gen", request.method, request.remote_addr)
	return render_template("email-gen.html")

@app.route('/email-gen/submit', methods=['POST'])
def email_gen_submit():
# 	before("email-gen/submit", request.method, request.remote_addr)
	FullName = request.form["name"]
	End = "@{}".format(request.form["domain"])
	Fname = FullName.split(" ")[0]
	Lname = FullName.split(" ")[1]
	e1 = (Fname + End).lower()
	e2 = (Fname[0] + Lname + End).lower()
	e3 = (Fname + "." + Lname + End).lower()
	e4 = (Fname + Lname + End).lower()
	return "{}, {}, {}, {}".format(e1, e2, e3, e4)

# Run
if __name__ == '__main__':
	app.run(debug = True)
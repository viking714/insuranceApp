"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,jsonify,request,redirect,session
from InsuranceApp import app


InsuranceDict = {1:{"name":"PingAn","age":"18-50","duration":"Whole Life","number":"120"},
				 2:{"name":"PingAnFu2019","age":"18-50","duration":"Whole Life","number":"100"}}


def loginCheck(func):
	def wrapper(*args,**kwargs):
		if session.get('user') != 'Joey' or session.get('pwd') != '123':
			return render_template('login.html')
		func(*args,**kwargs)
	return wrapper


@app.route('/home')
@loginCheck
def home():
    """Renders the home page."""

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
		insurance = InsuranceDict
    )

@app.route('/Detail/<int:nid>')
def detail(nid):
	info = InsuranceDict[nid]
	return render_template(
        'Detail.html',
		insuranceDetail = info
    )

@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user = request.form.get('user')
		password = request.form.get('password')
		session['user'] = user
		session['pwd'] = password
		if user == 'Joey' and password == '123':
			#redirect('/home')
			return render_template('index.html',title='Home Page',year=datetime.now().year,insurance = InsuranceDict)
		return render_template('login.html',error='user or password error')



@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

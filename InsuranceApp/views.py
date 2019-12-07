"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,jsonify
from InsuranceApp import app



InsuranceDict = {1:{"name":"PingAn","age":"18-50","duration":"Whole Life","number":"120"},
				 2:{"name":"PingAnFu2019","age":"18-50","duration":"Whole Life","number":"100"}}


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
		insurance = InsuranceDict
    )

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

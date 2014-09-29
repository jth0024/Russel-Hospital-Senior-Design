#Packages and sys
from rh import app
import os
from flask import jsonify, render_template, redirect, url_for, request, flash

#Our Modules
from sql_query import queryTable

#---------------------Sample Data-----------------------
#alerts 0-Completed, 1-Warning, 2-Critical
alerts = [
	{
		'id': 1,
		'type': 2,
		'date': u'Thursday 4-11-2014 at 7:44:57 PM',
		'description': u'Outside air damper error at AUH-ER1',
		'done': False
	},
	{
		'id': 2,
		'type': 1,
		'date': u'Friday 4-10-2014 at 2:40:53 PM',
		'description': u'High humidity at AUH-ER1',
		'done': False
	}
]
#Maintenance
maintenance = [
	{
		'id': 1,
		'target': u'Fire Extinguisher',
		'date': u'8-19-2014',
		'countdown': 74
	}
]

@app.route('/')
def index():
	return redirect(url_for('return_overview'))

@app.route('/rh/api/v1.0/alerts', methods = ['GET'])
def return_alerts():
	#Authenticate
	#populate alerts
	return render_template("alerts.html")

@app.route('/rh/api/v1.0/contact', methods = ['GET'])
def return_contact():
	#populate contact info
	return render_template("contact.html")

@app.route('/rh/api/v1.0/equipment', methods = ['GET'])
def return_equipment():
	#authenticate
	#populate equipment
	devices = queryTable("Devices")
	
	return render_template("equipment.html")

@app.route('/rh/api/v1.0/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		flash('login')
		return redirect(url_for('return_overview'))

	return render_template('login.html', error = error)

@app.route('/rh/api/v1.0/logout')
def logout():
	return 'logout'

@app.route('/rh/api/v1.0/maintenance', methods = ['GET'])
def return_maintenance():
	#authenticate
	#populate scheduled maintenance
	return jsonify( {'maintenance': maintenance} )

@app.route('/rh/api/v1.0/overview', methods = ['GET'])
def return_overview():
	#authenticate
	#populate summary reports
	#populate scheduled maintenance
	#populate recent alerts
	return render_template("index.html")

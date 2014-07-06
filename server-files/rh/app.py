#!flask/bin/python
import os
from flask import Flask, jsonify
from flask import url_for

app = Flask(__name__, static_url_path='')

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
	return 'Hello World!'

@app.route('/rh/api/v1.0/alerts', methods = ['GET'])
def return_alerts():
	return jsonify( {'alerts': alerts} )

@app.route('/rh/api/v1.0/contact', methods = ['GET'])
def return_contact():
	return 'RH contact'

@app.route('/rh/api/v1.0/equipment', methods = ['GET'])
def return_equipment():
	return 'RH equipment'

@app.route('/rh/api/v1.0/maintenance', methods = ['GET'])
def return_maintenance():
	return jsonify( {'maintenance': maintenance} )

@app.route('/rh/api/v1.0/overview', methods = ['GET'])
def return_overview():
	return 'RH overview'

if __name__ == '__main__':
	app.run(debug = True)
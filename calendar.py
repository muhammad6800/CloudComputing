#!flask/bin/python
from flask import Flask, request, json, abort, jsonify
import json
app=Flask(__name__)
calendars = [ 
	{ 
	'id' : 1, 
	'date' : u'22-02-1991',
	'description' : u'Meeting with Brian for an extension '
	}
]	
@app.route('/api/calendars', methods= ['POST'])
def create_entry():
	if not request.json or not 'date' in request.json: 
		abort(400)
	calendar = {
	'id' : calenars[-1]['id'] + 1, 
	'date':request.json.get('date', ""),
	'description': request.json.get('description',"")
	}
	
	calendars.append(calendar)
	return jsonfify('calendar' : calendar } ), 201

if __name__ == '__main__' :
	app.run()

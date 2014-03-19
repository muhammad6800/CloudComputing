#!flask/bin/python 
from flask import Flask, jsonify ,request, abort
import json
app = Flask(__name__)
calendar={
'lilcal':[ 	
	{
	
		'userid':0, 
		'date': u'19/2/2014' , 
		'description': u'Meet Moe ' , 
#		'starttime': u'14:00' , 
#		'endtime': u'16:00',
#		'repeats': u'Monthly',
#		'location': u'www.google.com/map' ,
	}

]
}

	

@app.route('/calendar/<int:userid>', methods = ['GET'] ) 
def getuserid(userid):
	calendars = filter(lambda t:t['userid'] == userid, calendar)
	if len(calendar) == 0:
		abort(404)
	return jsonify ( { 'calendar' : calendars[0] } )

@app.route('/calendar',methods=['GET'])
def get_entry():
	return jsonify({'calendar':calendar})

#@app.route('/getID',methods=['POST'])
#def add_entry():
#	if not request.json or not 'date' in request.json: 
#		abort(400)	
#	temp = { 
#		'date' : request.json('date',"")
	#	'userid' : calendar[-1]['userid']+1
	#	}
	
#	calender.append(temp)
#	return jsonify({'calender':temp}),201		


@app.route('/calendars/<int:user_id>', methods= ['PUT'])
def update_task(userid):
	calendar = filter(lambda t: t['id'] == userid, calendars)
	if len(calendar) == 0: 
		abort(404)
	if not request.json: 
		abort(400)
	if 'date' in request.json and type(request.json['date']) != unicode:
		abort(400)
	if 'description' in request.json and type(request.json['description']) != unicode: 
		abort(400)	
	calendar[0]['date'] = request.json.get('date', calendar[0]['date'])
#	calendar[0]['description'] = request.json.get('description', calendar[0]['description'])
	return jsonify({'calendar':calendar[0]} )

@app.route('/calenders/delete/<int:user_id>', methods=['DELETE'])
def delete_task(userid):
	temp = filter(lambda t:t['id'] ==userid,calender)
	if	len(temp) == 0:
		abort(404)

	calender.remove(temp[0])
	return jsonify({'result':TRUE})

if __name__== '__main__':
	app.run()  

		

#! python

import json
from flask import Flask, request, make_response, send_file 
from hasher import compute_hash
from fileservicefactory import get_file_service, FIREBASE, SYSTEM

app = Flask(__name__)

fileservice = get_file_service(SYSTEM)

@app.route('/')
def index():
	return make_response({"message": "hello from Flask"}, 200)


@app.route('/files', methods=['POST', 'GET'])
def upload_file():
	if(request.method == "POST"):
		f = request.files['file']
		hash = fileservice.save_file(f)
		return make_response(str(hash), 201)
	elif(request.method == "GET"):
		filename = request.args["file"]
		if(not filename):
			return make_response('Bad request', 400)
		result, path = fileservice.search_file(filename)
		if(result):
			return send_file(path, as_attachment=True)
		else:
			return make_response('File not found', 404)

@app.route('/draw', methods=['POST'])
def draw():
	from pymupdfwrapper import draw_on_pdf
	draw_data = request.files['draw'].read()
	draw_json_data = json.loads(draw_data)
	base_file = draw_json_data['baseFile']
	if(not fileservice.search_file(base_file)[0]):
		return make_response('Base file not found.', 400)
	drawing_detail = draw_json_data['draw']
	out_file_name = compute_hash(draw_data)
	result = draw_on_pdf(base_file, drawing_detail, out_file_name)
	if(result[0]):
		return make_response(out_file_name, 200)
	else:
		return make_response(result[1], 500)
#! python

import json
from flask import Flask, request, make_response, send_file 
from hasher import compute_hash

app = Flask(__name__)

@app.route('/')
def index():
	return make_response({"message": "hello from Flask"}, 200)

def _save_file(file_storage_object):
	fstream = file_storage_object.read()
	print(fstream)
	hash = compute_hash(fstream)
	print(hash)
	f = open(hash, 'wb')
	f.write(fstream)
	f.close()
	return hash


def _search_file(filename):
	import os
	if(filename in os.listdir('.')):
		return (True,filename)
	else:
		return (False, 'Not found')
 
@app.route('/files', methods=['POST', 'GET'])
def upload_file():
	if(request.method == "POST"):
		f = request.files['file']
		hash = _save_file(f)
		return make_response(str(hash), 201)
	elif(request.method == "GET"):
		filename = request.args["file"]
		if(not filename):
			return make_response('Bad request', 400)
		result, path = _search_file(filename)
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
	if(not _search_file(base_file)[0]):
		return make_response('Base file not found.', 400)
	drawing_detail = draw_json_data['draw']
	out_file_name = compute_hash(draw_data)
	result = draw_on_pdf(base_file, drawing_detail, out_file_name)
	if(result[0]):
		return make_response(out_file_name, 200)
	else:
		return make_response(result[1], 500)
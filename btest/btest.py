#!/usr/bin/env python
#encoding=utf-8
import bottle,os,datetime,random
from bottle import route, run, template,request,response,view,static_file

def _gen_current_rand():
	dt = datetime.datetime.now()
	return dt.strftime("%Y%m%d_%H%M%S_")+str(random.randint(100,999))

@route('/uploads/:filename')
def upload_show(filename):
	return static_file(filename,root="uploads")
	

@route('/upload')
def upload():
	return template('upload')

@route('/upload', method='POST')
def do_upload():
	ret = {}
	name = request.forms.name
	data = request.files.data
	if data and data.file:
		raw = data.file.read() # This is dangerous for big files
		filename = data.filename
		name, ext = os.path.splitext(filename)
		filename = _gen_current_rand()+ext
		save_path = os.path.join(os.getcwd(),"uploads")
		save_path = os.path.join(save_path,filename)
		f = open(save_path,'wb')
		f.write(raw)
		f.close()
		ret["filename"] = filename
		ret["rel_path"] = "/uploads/"+filename
		ret["abs_path"] = "http://192.168.201.75:8000" + ret["rel_path"]
		#return  "Hello %s! You uploaded %s (%d bytes)." % (name, filename, len(raw))
		ret["msg"] = "ok"
	else:
		ret["msg"] = "not ok"
	return ret


@route('/',method=['GET','POST'])
def home():
	bottle.redirect('/home2')

@route('/json')
def json():
	ret = {}
	ret["msg"] = "ok"
	return ret

@route('/home2')
def home2():
	return template('home2')

@route('/home3')
def home3():
	return template('home3')

@route('/home3',method='POST')
def home3_post():
	return bottle.redirect('/home2')

app = bottle.default_app()
app.autojson = True
run(app = app,reloader = False,host='0.0.0.0',port = 8000)

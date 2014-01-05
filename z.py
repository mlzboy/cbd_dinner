#!/usr/bin/env python
#encoding=utf-8
import bottle
from bottle import route, run, template,request,response,view,static_file
import os.path,sys,shutil,os
reload(sys)
os.chdir(os.path.dirname(__file__))
sys.setdefaultencoding('utf8')
path=os.path.join(os.getcwd(),"cbd")
print path
sys.path.append(path)
from django.core.management import setup_environ
import settings
setup_environ(settings)
from dinner.models import *
from django.db.models import Q
import codecs
from beaker.middleware import SessionMiddleware

@route('/static/:fname#.*#')
def static(fname):
    return static_file(fname, root='static')

@route('/is_login')
def is_login():
	ret = {}
	if _is_login():
		ret["is_login"] = True
		ret["username"] = _get_username()
		ret["msg"] = "ok"
	else:
		ret["msg"] = "not ok"
	print ret["msg"]
	response.add_header("Access-Control-Allow-Origin","*");
	response.add_header("Access-Control-Allow-Headers","Authorization,Accept,Origin,Content-Type,If-Match");
	response.add_header("Access-Control-Allow-Methods","GET,OPTIONS,POST,PUT,DELETE,PATCH");
	response.add_header("Allow","GET,POST,PUT,HEAD,DELETE,TRACE,COPY,LOCK,MKCOL,MOVE,PROPFIND,PROPPATCH,UNLOCK,REPORT,MKACTIVITY,CHECKOUT,MERGE,M-SEARCH,NOTIFY,SUBSCRIBE,UNSUBSCRIBE,PATCH");
	return ret

def auth(handler):
 	def _check_auth(*args,**kwargs):
		if _is_login():
			return handler(*args,**kwargs)
		else:
			url = request.params.url	
			bottle.redirect('/login?url=%s'%url)
	return _check_auth

def _is_login():
	session = bottle.request.environ["beaker.session"]
	if "username" in session:
		return True
	else:
		return False

def _logout():
	session = bottle.request.environ["beaker.session"]
	if "username" in session:
		del session["username"]
	

def _get_username():
	session = bottle.request.environ["beaker.session"]
	if "username" in session:
		return session["username"]
	return None

def _load_view(path):
	lines=[]
	for line in codecs.open(path,"r","utf-8").readlines():
		lines.append(line)
	ret = "".join(lines)
	return ret


@route('/logout')
def logout():
	ret = {}
	if _is_login():
		_logout()
		ret["msg"] = "ok"
	else:
		ret["msg"] = "not ok"
	return ret

@route('/register')
def register():
	#return _load_view("./views.bak/register2.html")
	return _load_view("/home/mlzboy/work/code/cbd/views.bak/register2.html")
	#return template('register')

@route('/register',method='POST')
def register_post():
	ret = {}
	print "register_post"
	print request.json
	for elem in request.headers:
		print elem
	print request.content_type
	f=request.body
	for line in f:
		print line
	print request.forms
	username = request.forms["username"].lower().strip()
	passwd   = request.forms["passwd"].lower().strip()
	if User.objects.filter(username = username).count() == 0:
		session = bottle.request.environ["beaker.session"]
		session["username"] = username	
		User.objects.create(username = username, passwd = passwd)
		ret["msg"] = "ok"
	else:
		ret["msg"] = "not ok"

	for elem in request.forms:
		print elem,request.forms[elem]
	print ret["msg"]
	#return ret
	response.add_header("Access-Control-Allow-Origin","*");
	response.add_header("Access-Control-Allow-Headers","Authorization,Accept,Origin,Content-Type,If-Match");
	response.add_header("Access-Control-Allow-Methods","GET,OPTIONS,POST,PUT,DELETE,PATCH");
	response.add_header("Allow","GET,POST,PUT,HEAD,DELETE,TRACE,COPY,LOCK,MKCOL,MOVE,PROPFIND,PROPPATCH,UNLOCK,REPORT,MKACTIVITY,CHECKOUT,MERGE,M-SEARCH,NOTIFY,SUBSCRIBE,UNSUBSCRIBE,PATCH");
	return ret

@route('/login')
def login():
	print "login page"
	return template('login')

@route('/login',method='POST')
def login_post():
	ret = {}
	username = request.forms["username"].lower().strip()
	passwd   = request.forms["passwd"].lower().strip()
	url   = request.forms["url"]
	if url.count("?url=") > 0:
		a,b = url.split("?url=")
		url = b
	else:
		url = ""
	ret["url"] = url;
	if User.objects.filter(username = username).count() == 1:
		session = bottle.request.environ["beaker.session"]
		session["username"] = username
		ret["msg"] = "ok"
	else:
		ret["msg"] = "not ok"
	print ret["msg"]
	print "login_post"
	response.add_header("Access-Control-Allow-Origin","*");
	response.add_header("Access-Control-Allow-Headers","Authorization,Accept,Origin,Content-Type,If-Match");
	response.add_header("Access-Control-Allow-Methods","GET,OPTIONS,POST,PUT,DELETE,PATCH");
	response.add_header("Allow","GET,POST,PUT,HEAD,DELETE,TRACE,COPY,LOCK,MKCOL,MOVE,PROPFIND,PROPPATCH,UNLOCK,REPORT,MKACTIVITY,CHECKOUT,MERGE,M-SEARCH,NOTIFY,SUBSCRIBE,UNSUBSCRIBE,PATCH");
	return ret


@route('/')
def home():
	"""
	根据session["filter"]条件进行过滤返回数据
	"""
	return template('whole')
	
@route('/filters')
def filters_():
	return template('filters')

@route('/filters',method='POST')
def filters_post():
	"""
	构建筛选条件
	"""
	ret = {}
	ret["msg"] = "ok"
	filters = {}
	print "filters post"
	for elem in request.forms:
		val = request.forms[elem]
		if val <> "全部":
			filters[elem] = val;
			print "cond:",elem,val
	#TODO:
	users = User.objects.all()
	#through filters get result json data
	str = template("_home_list",users = users)
	print str
	ret["html"] = str
	return ret

def user2dict(user):
	"""
	convert django model object to json dict
	"""
	ret = {}
	ret["intro"] = user.intro
	ret["hometown"] = user.hometown
	ret["photo1"] = user.photo1
	ret["username"] = user.username
	return ret


@route('/profilett')
def profile_xxxbyt_id():
	return "hhhhhh"

@route('/profilet')
def profile_xxxby_id():
	return "hhhhhh"

@route('/profile/:id')
def profile_by_id(id):
	ret = {}
	u = User.objects.get(id = id);
	print u
	if u:
		print u
		ret["msg"] = "ok"
		ret["user"] = user2dict(u)
	else:
		ret["msg"] = "not ok"
	return ret


@route('/profile')
@auth
def profile():
	"""
	/profile/username
	"""
	username = _get_username()
	session = bottle.request.environ["beaker.session"]
	print type(session)
	print "sessionid",session.id
	return username

@route('/basic_profile')
@auth
def basic_profile():
	print "basic_profile"
	return template('basic_profile')

@route('/basic_profile',method='POST')
@auth
def basic_profile_post():
	print "basic_profile_post"
	ret = {}
	username = _get_username()
	user1 = User.objects.filter(username = username).all()[0]
	for elem in request.forms:
		if hasattr(user1,elem):
			val = request.forms[elem]
			setattr(user1,elem,val)
			print elem,"=>",val,type(val)
	user1.save()
	ret["msg"] = "ok"
	return ret


if __name__ == "__main__":
	session_opts = {
		"session.type": "file",
		'session.cookie_expires': True,
		'session.auto': True,
		'session.data_dir': "cache",
	}

	app = bottle.default_app()
	app.autojson = True
	app = SessionMiddleware(app, session_opts)
	run(app = app,reloader = False,host='0.0.0.0',port = 80)

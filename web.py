#!/usr/bin/env python
#encoding=utf-8
import json
import bottle
from bottle import route, run, template,request,response,static_file
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
import redis
r = redis.Redis()

def get_model_by_pkid(model_name,model_pkid):
	return r.hgetall("%s:id=%s"%(model_name,model_pkid))

def get_model_ids(model_name,field_table_name,field_name,field_val):
	return r.smembers("%s:%s__%s=%s"%(model_name,field_table_name,field_name,field_val))

def set_model(model_name,dict_val):
	r.hmset("%s:id=%s"%(model_name,dict_val["id"]),dict_val)

def auth(handler):
	def _check_auth(*args,**kwargs):
		if _is_login():
			return handler(*args,**kwargs)
		else:
			bottle.redirect('/login')
	return _check_auth

@route('/pay/:dinner_id')
def pay(dinner_id):
	dinner = r.hgetall("dinner:id=%s"%dinner_id)
	for key,v in dinner.iteritems():
		print key,v
	user_creator_id = dinner["user_creator"]
	rest_id = dinner["rest_id"]
	rest = r.hgetall("rest:id=%s"%rest_id)
	dinner_creator = r.hgetall("user:id=%s"%user_creator_id)
	return template("pay",dinner = dinner, dinner_creator = dinner_creator , rest = rest)

@route('/pay/:dinner_id',method='POST')
@auth
def pay_post(dinner_id):
	applier_id = _get_userid()
	pay = dict()
	pay["user_id"] = applier_id
	pay["dinner_id"] = dinner_id
	pay["money"] = "25"
	r.lpush("pay:user_id=%s"%applier_id,dict)
	dinner = r.hgetall("dinner:id=%s"%dinner_id)
	dinner_creator_id = dinner["user_creator"]
	user_creator_id = dinner["user_creator"]
	#pay success
	#pay redirect to dinner_creator profile page
	#send applier msg to dinner creator
	msg = dict()
	msg ["text"] = "aplly dinner with you"
	msg ["user_id"] = applier_id
	msg ["dinner_id"] = dinner_id
	r.lpush("message:id=%s"%user_creator_id,msg)
	bottle.redirect("/profile/%s"%user_creator_id)


@route('/uploads/:fname#.*#')
def static(fname):
	return static_file(fname, root='uploads')

@route('/static/:fname#.*#')
def static(fname):
	return static_file(fname, root='static')


def _convert_datetime(str_date,fmt="%Y-%m-%d %H:%M:%S"):
	"""
	convert string to date
	"""
	return datetime.strptime(str_date, fmt)

@route('/is_login')
def is_login():
	ret = {}
	if _is_login():
		ret["is_login"] = True
		ret["username"] = _get_username()
		ret["msg"] = "ok"
	else:
		ret["msg"] = "not ok"
	return ret


def _is_login():
	session = bottle.request.environ["beaker.session"]
	if "username" in session:
		return True
	else:
		return False

def _get_username():
	session = bottle.request.environ["beaker.session"]
	if "username" in session:
		return session["username"]
	return None

def _get_userid():
	session = bottle.request.environ["beaker.session"]
	if "userid" in session:
		return session["userid"]
	return None

def _load_view(path):
	lines=[]
	for line in codecs.open(path,"r","utf-8").readlines():
		lines.append(line)
	ret = "".join(lines)
	return ret

@route('/message/:msg_id')
def message(msg_id):
	"""
	msg details
	"""
	pass


@route('/messages/:user_id')
def message(user_id):
	#fetch last 3 message
	NUM = 3
	user_id = _get_userid() or user_id
	print "user_id=>",user_id
	key = "message:user__receiver_id=%s"%user_id
	msg_ids = list(r.smembers(key))
	msg_ids = get_model_ids("message","user","receiver_id",user_id)

	print msg_ids
	msgs = []
	for msg_id in msg_ids:
		msg = r.hgetall("message:id=%s"%msg_id)
		msg = get_model_by_pkid("message",msg_id)
		print msg
		user__from_id = msg["user__fromer_id"]
		msg["user"] = r.hgetall("user:id=%s"%user__from_id)
		msg["user"] = get_model_by_pkid("user",user__from_id)
		msg["dinner"] = r.hgetall("dinner:id=%s"%msg["dinner_id"])
		msg["dinner"] = get_model_by_pkid("dinner",msg["dinner_id"])
		print "++++"
		msgs.append(msg)
	print "==========="
	return template('message',msgs = msgs)


@route('/logout')
def logout():
	session = bottle.request.environ["beaker.session"]
	if "username" in session:
		del session["username"]
	return bottle.redirect('/')

@route('/register')
def register():
	#return _load_view("./views/register.html")
	return template('register')

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
	if User.objects.filter(username = username).count() == 1:
		user = User.objects.filter(username = username).all()[0]
		session = bottle.request.environ["beaker.session"]
		session["username"] = username
		session["userid"] = user.id
		ret["msg"] = "ok"
	else:
		ret["msg"] = "not ok"
	print ret["msg"]
	print "login_post"
	return ret


@route('/')
def home():
	"""
	根据session["filter"]条件进行过滤返回数据
	"""
	tpl =  _load_view("./views/home.html")
	ret = {}
	ret["is_login"] = _is_login()
	ret["username"] = _get_username()
	return template('home', ret)

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

	session = bottle.request.environ["beaker.session"]
	session["filters"] = filters
	print session["filters"]
	#return ret
	#return "<script>window.location.href='/';</script>"
	#bottle.redirect('http://192.168.201.75/')
	#response.content_type = 'text/html; charset=utf-8'
	#return template("redirect",url = 'http://192.168.201.75/')
	return bottle.redirect("/?a=11")

@route('/personal')
def personal():
	#get this user entry json data
	user = r.hgetall("user:id=1")
	dinner_ids = r.sinter("dinner:user_creator=1","dinner:empty=true")
	#filter dinner_ids by startdate greater than today
	#and order by create peronal ranking score
	dinners = []
	for dinner_id in dinner_ids:
		dinner = r.hgetall("dinner:id=%s"%dinner_id)
		dict = json.loads(dinner)
		if _convert_datetime(dict["created_on"]) > datetime.datetime.now():
			dinners.append(dinner)
	print user,dinners
	return template("personal",user = user ,dinners = dinners)



@route('/profile/:user_id')
def profile_new(user_id):
	user = r.hgetall("user:id=%s"%user_id)
	key = "dinner:user_creator=%s"%user_id
	size = r.llen("key")
	#dinner_ids = r.lrange(key,0,size-1)
	dinner_ids = r.smembers(key)
	dinners = []
	for dinner_id in dinner_ids:
		dinner = r.hgetall("dinner:id=%s"%dinner_id)
		rest_id = dinner["rest_id"]
		user_creator_id = dinner["user_creator"]
		user_creator = r.hgetall("user:id=%s"%user_creator_id)
		dinner["user_creator"] = user_creator
		rest = r.hgetall("rest:id=%s"%rest_id)
		dinner["rest"] = rest
		dinners.append(dinner)

	#privliage control 
	return template('profile_new',user = user,dinners = dinners)

@route('/profile')
@auth
def profile():
	"""
	/profile/username
	"""
	username = _get_username()
	#get this user entry json data
	user = r.hget("user:id=1")
	dinners_ids = r.get("dinner:user_creator=1")
	#through current date
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
	run(app = app,reloader = True,host='0.0.0.0',port = 80)

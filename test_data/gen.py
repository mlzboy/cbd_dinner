#!/usr/bin/env python
#encoding=utf-8
import redis,json,datetime
r=redis.Redis()
r.flushdb()
#in redis all were string
user = dict()
user["id"]="1"
user["username"]="1"
user["nickname"]="xiao 1"
user["password"]="1"
user["created_on"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user["photo1"] = "/uploads/album-bb.jpg"
user["gender"] = "male"
user["high"]="175cm"
user["weight"]="80kg"
user["education"]="master"
user["career"]="engineer"
user["intro"]="nothing more"
user["company"]="jd"
user["sign"]="sign"
user["state"]="state"
user["born"]="yiwu"
user["hobby"]="swimming"


print user
print json.dumps(user)
r.hmset("user:id=%s"%user["id"],user)

user = dict()
user["id"]="2"
user["username"]="2"
user["nickname"]="xiao 2"
user["password"]="2"
user["created_on"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user["photo1"] = "/uploads/album-bb.jpg"
user["gender"] = "male"
user["high"]="175cm"
user["weight"]="80kg"
user["education"]="master"
user["career"]="engineer"
user["intro"]="nothing more"
user["company"]="jd"
user["sign"]="sign"
user["state"]="state"
user["born"]="yiwu"
user["hobby"]="swimming"

print user
print json.dumps(user)
r.hmset("user:id=%s"%user["id"],user)

user = dict()
user["id"]="3"
user["username"]="3"
user["nickname"]="xiao 3"
user["password"]="3"
user["created_on"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user["photo1"] = "/uploads/album-bb.jpg"
user["gender"] = "male"
user["high"]="175cm"
user["weight"]="80kg"
user["education"]="master"
user["career"]="engineer"
user["intro"]="nothing more"
user["company"]="jd"
user["sign"]="sign"
user["state"]="state"
user["born"]="yiwu"
user["hobby"]="swimming"

print user
print json.dumps(user)
r.hmset("user:id=%s"%user["id"],user)

user = dict()
user["id"]="4"
user["username"]="4"
user["nickname"]="xiao 4"
user["password"]="4"
user["created_on"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user["photo1"] = "/uploads/album-bb.jpg"
user["gender"] = "male"
user["high"]="175cm"
user["weight"]="80kg"
user["education"]="master"
user["career"]="engineer"
user["intro"]="nothing more"
user["company"]="jd"
user["sign"]="sign"
user["state"]="state"
user["born"]="yiwu"
user["hobby"]="swimming"

print user
print json.dumps(user)
r.hmset("user:id=%s"%user["id"],user)


#restaurant
rest = dict()
rest["id"] = "1"
rest["name"] = "startbucks"
rest["place"] = "location xxx"
rest["phone"] = "010-xxx"
r.hmset("rest:id=%s"%rest["id"],rest)


#dinner
print "dinner"
dinner = dict()
dinner["desc"]="AA"
dinner["id"] = "1"
dinner["rest_id"] = "1"
dinner["purpose"] = "hello kitty"
dinner["full"] = "false"
dinner["created_on"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
delta = datetime.timedelta(days=3)
dinner["eat_on"] = (datetime.datetime.now() + delta).strftime("%Y-%m-%d %H:%M:%S")
dinner["user_creator"] = "1"
print dinner
print json.dumps(dinner)
r.hmset("dinner:id=%s"%dinner["id"],dinner)
#
#r.sadd("dinner:full=false","1")
#r.sadd("dinner:user_createor=1","1")
#print r.sinter("dinner:full=false","dinner:user_createor=1")

dinner = dict()
dinner["desc"]="AA"
dinner["id"] = "2"
dinner["purpose"] = "hello kitty"
dinner["full"] = "false"
dinner["created_on"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
delta = datetime.timedelta(days=3)
dinner["eat_on"] = (datetime.datetime.now() + delta).strftime("%Y-%m-%d %H:%M:%S")
dinner["user_creator"] = "2"
r.hmset("dinner:id=%s"%dinner["id"],dinner)


dinner = dict()
dinner["desc"]="AA"
dinner["id"] = "3"
dinner["purpose"] = "hello kitty"
dinner["full"] = "false"
dinner["created_on"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
delta = datetime.timedelta(days=3)
dinner["eat_on"] = (datetime.datetime.now() + delta).strftime("%Y-%m-%d %H:%M:%S")
dinner["user_creator"] = "3"
r.hmset("dinner:id=%s"%dinner["id"],dinner)

dinner = dict()
dinner["desc"]="AA"
dinner["id"] = "4"
dinner["purpose"] = "hello kitty"
dinner["full"] = "false"
dinner["created_on"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
delta = datetime.timedelta(days=3)
dinner["eat_on"] = (datetime.datetime.now() + delta).strftime("%Y-%m-%d %H:%M:%S")
dinner["user_creator"] = "4"
r.hmset("dinner:id=%s"%dinner["id"],dinner)




r.lpush("dinner:user_creator=1","1")
r.lpush("dinner:user_creator=2","2")
r.lpush("dinner:user_creator=3","3")
r.lpush("dinner:user_creator=4","4")



#msg

msg = dict()
#msg["user_applier"] = "4"
msg["id"] = "1"
msg["user__fromer_id"] = "4"#user_from
msg["dinner_id"] = "1"
msg["text"]="apply dinner with you"
r.hmset("message:id=%s"%msg["id"],msg)
r.sadd("message:user__receiver_id=1",msg["id"])
#r.lpush("message:user_id=1",msg)

msg = dict()
#msg["user_creator"] = "2"
msg["id"] = "2"
msg["user__fromer_id"] = "2"
msg["dinner_id"] = "2"
msg["text"] = "agree dinner with you"
r.hmset("message:id=%s"%msg["id"],msg)
#r.lpush("message:user_id=1",msg)
r.sadd("message:user__receiver_id=1",msg["id"])

msg = dict()
#msg["user_creator"] = "3"
msg["id"] = "3"
msg["user__fromer_id"] = "3"
msg["dinner_id"] = "3"
msg["text"] = "refused dinner with you"
r.hmset("message:id=%s"%msg["id"],msg)
#r.lpush("message:user_id=1",msg)
r.sadd("message:user__receiver_id=1",msg["id"])

#apply
#user_applier,#dinner_id

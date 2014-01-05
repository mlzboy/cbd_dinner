#encoding=utf-8
from django.db import models

# Create your models here.
class Dinner(models.Model):
	purpose = models.CharField(max_length = 400,null = True,blank = True)#目的
	count = models.IntegerField(default = 2,db_index = True)#人数
	girl_count = models.IntegerField(default = -1,db_index = True)
	boy_count = models.IntegerField(default = -1,db_index = True)
	location = models.CharField(max_length=400,null=True,blank=True)
	time = models.DateTimeField()
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)

class DinnerApplier(models.Model):
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)

class Message(models.Model):
	to = models.CharField(max_length=40,null=True,blank=True)
	msg = models.CharField(max_length=400,null=True,blank=True)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)

class User(models.Model):
	username = models.CharField(max_length=40,null=True,blank=True)
	passwd = models.CharField(max_length=400,null=True,blank=True)
	intro = models.CharField(max_length=400,null=True,blank=True)
	hometown = models.CharField(max_length=40,null=True,blank=True)# jiguan
	qq = models.CharField(max_length=40,null=True,blank=True)# qq
	sina = models.CharField(max_length=40,null=True,blank=True)# sina weibo
	wechat = models.CharField(max_length=40,null=True,blank=True)# weixin
	industry = models.CharField(max_length=40,null=True,blank=True)# hanye
	career = models.CharField(max_length=40,null=True,blank=True)# career
	interest = models.CharField(max_length=40,null=True,blank=True)
	photo1 = models.CharField(max_length=40,null=True,blank=True)
	photo2 = models.CharField(max_length=40,null=True,blank=True)
	coordinate = models.CharField(max_length=40,null=True,blank=True)# zuobiao
	born = models.DateTimeField(null=True,blank=True)#born
	edu = models.CharField(max_length=40,null=True,blank=True)#xueli
	returned = models.BooleanField(default=False)#haigui
	gender = models.BooleanField(default=True)#T男
	forgen = models.BooleanField(default=False)#waiqi
	soe = models.BooleanField(default=False) #guoqi
	civil = models.BooleanField(default=False) #gongwuyuan
	institution = models.BooleanField(default=False) #shiyedanwei
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)




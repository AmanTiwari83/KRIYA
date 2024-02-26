from django.db import models

# Create your models here.
class recentblog(models.Model):
    rbpic=models.ImageField(upload_to='static/rbimage/',null=True)
    rbday=models.CharField(max_length=100,null=True)
    rbmonth=models.CharField(max_length=100,null=True)
    rbname=models.CharField(max_length=100,null=True)
    rbncomm=models.IntegerField(null=True)

class team(models.Model):
    tname=models.CharField(max_length=100,null=True)
    tpost=models.CharField(max_length=100,null=True)
    timg=models.ImageField(upload_to='static/teamimage/',null=True)
    theading=models.TextField(null=True)

class event(models.Model):
    eday=models.IntegerField(null=True)
    eyear=models.IntegerField(null=True)
    emonth=models.CharField(max_length=100,null=True)
    etime=models.CharField(max_length=100,null=True)
    eplace=models.CharField(max_length=100,null=True)
    ecity=models.CharField(max_length=100,null=True)
    epic=models.ImageField(upload_to='static/eventimage/',null=True)

class registers(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Password=models.CharField(max_length=100,null=True)
    Contact=models.CharField(max_length=25,null=True)
    Picture=models.ImageField(upload_to='static/register/',null=True)
    Address=models.TextField(null=True)

class sign(models.Model):
    User=models.CharField(max_length=100,null=True)
    Password=models.CharField(max_length=100,null=True)

class contactus(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Contact=models.IntegerField(null=True)
    Address=models.TextField(null=True)
    Message=models.TextField(null=True)

class aboutus(models.Model):
    user=models.IntegerField(null=True)
    exp=models.IntegerField(null=True)
    branch=models.IntegerField(null=True)

class newevent(models.Model):
    eday=models.IntegerField(null=True)
    eyear=models.IntegerField(null=True)
    emonth=models.CharField(max_length=100,null=True)
    etime=models.CharField(max_length=100,null=True)
    eplace=models.CharField(max_length=100,null=True)
    ecity=models.CharField(max_length=100,null=True)
    ehead=models.TextField(null=True)
    epic=models.ImageField(upload_to='static/eventimage/',null=True)

class detail(models.Model):
    name=models.CharField(max_length=100,null=True)
    mob=models.IntegerField(null=True)
    pic=models.ImageField(upload_to='static/booknow/',null=True)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(null=True)

class thought(models.Model):
    para=models.TextField(null=True)
    pic=models.ImageField(upload_to='static/thoughts/',null=True)
    name=models.CharField(max_length=100,null=True)
    prof=models.CharField(max_length=200,null=True)

class footer(models.Model):
    fft=models.CharField(max_length=100,null=True)
    fst=models.CharField(max_length=100,null=True)
    sft=models.CharField(max_length=100,null=True)
    sst=models.CharField(max_length=100,null=True)


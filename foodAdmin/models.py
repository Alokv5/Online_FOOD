from django.db import models

from django.db import models

class StateModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,unique=True)
    photo=models.ImageField(upload_to='state_images/')


class CityModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='city_images/')
    city_state = models.ForeignKey(StateModel, on_delete=models.CASCADE)


class CusineModel(models.Model):
    id=models.AutoField(primary_key=True)
    type = models.CharField(max_length=100,unique=True)
    photo = models.ImageField(upload_to='cusine_images/')


class AdminLoginModel(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    otp=models.IntegerField(default=1234)






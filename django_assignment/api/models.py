from django.db import models

# Create your models here.
class Country(models.Model):
    id =  models.IntegerField(primary_key=True)
    Name = models.CharField(unique=True ,max_length=100)
    Description =  models.TextField()
    Population =  models.IntegerField()
    GDP =  models.FloatField()

class State(models.Model):
    id=  models.IntegerField(primary_key=True)
    Country=  models.ForeignKey(Country,on_delete=models.CASCADE)
    Name=  models.CharField(unique=True,editable=False,max_length=100)
    Description=  models.TextField()
    Population=  models.IntegerField()
    GDP=  models.FloatField()

class City(models.Model):
    id=models.IntegerField(primary_key=True)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    Country= models.ForeignKey(Country, on_delete=models.CASCADE)
    Description=models.TextField()
    Population=models.IntegerField()
    GDP=models.FloatField()
    Pin_Code=models.CharField(max_length=100)

class Town(models.Model):
    id=models.IntegerField(primary_key=True)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    Country= models.ForeignKey(Country, on_delete=models.CASCADE)
    Description=models.TextField()
    Population=models.IntegerField()
    GDP=models.FloatField()
    Pin_Code=models.CharField(max_length=100)

class Person(models.Model):
    id=models.IntegerField(primary_key=True)
    Name=models.CharField(unique=True,editable=False,max_length=100)
    City=models.ForeignKey(City,on_delete=models.CASCADE)
    Town=models.ForeignKey(Town,on_delete=models.CASCADE)
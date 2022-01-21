from django.db import models

class Employee(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	post=models.CharField(max_length=200)
	emp_id=models.IntegerField()
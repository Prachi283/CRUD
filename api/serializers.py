from rest_framework import serializers
from .models import Employee

class EmpSerializer(serializers.Serializer):
	name=serializers.CharField(max_length=200)
	email=serializers.EmailField(max_length=200)
	post=serializers.CharField(max_length=200)
	emp_id=serializers.IntegerField()

	def create(self,validated_data):
		return Employee.objects.create(**validated_data)

	def update(self,instance,validated_data):
		print(instance.name)
		instance.name=validated_data.get('name',instance.name)
		print(instance.name)
		instance.email=validated_data.get('email',instance.email)
		instance.post=validated_data.get('post',instance.post)
		instance.emp_id=validated_data.get('emp_id',instance.emp_id)
		instance.save()
		return instance
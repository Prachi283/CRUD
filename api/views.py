from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmpSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def employee_api(request):
	if request.method =="GET":
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		id=pythondata.get('id',None)
		if id is not None:
			emp = Employee.objects.get(id=id)
			serializer= EmpSerializer(emp)
			json_data=JSONRenderer().render(serializer.data)
			return HttpResponse(json_data,content_type='application/json')

		emp = Employee.objects.all()
		serializer=EmpSerializer(emp, many=True)
		json_data=JSONRenderer().render(serializer.data)
		return HttpResponse(json_data,content_type='application/json')

	if request.method=="POST":
		json_data=request.body
		stream = io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		serializer=EmpSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res= {'msg':'Data is Created'}
			json_data=JSONRenderer().render(res)
			return HttpResponse(json_data,content_type='application/json')
		json_data=JSONRenderer().render(serializers.errors)
		return HttpResponse(json_data,content_type='application/json')
		
	if request.method=="PUT":
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		id=pythondata.get('id')
		emp=Employee.objects.get(id=id)
		serializer=EmpSerializer(emp,data=pythondata,partial=True)
		if serializer.is_valid():
			serializer.save()
			res={'msg':'Data is Updated'}
			json_data=JSONRenderer().render(res)
			return HttpResponse(json_data,content_type='application/json')
		json_data=JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application/json')
			
	if request.method=="DELETE":
		json_data=request.body
		stream=io.BytesIO(json_data)
		pythondata=JSONParser().parse(stream)
		id= pythondata.get('id')
		emp=Employee.objects.get(id=id)
		emp.delete()
		res={'msg':'Data is Deleted'}
		json_data=JSONRenderer().render(res)
		return HttpResponse(json_data,content_type='application/json')

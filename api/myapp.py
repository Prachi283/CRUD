import requests
import json

URL= "http://127.0.0.1:8000/employeeapi/"

# Read Data
def get_data(id=None):
	data={}
	if id is not None:
		data={'id':id}
	json_data=json.dumps(data)
	r= requests.get(url= URL,data=json_data)
	data=r.json()
	print(data)

# Create Data
def post_data():
	data= {
		'name':'Shraddha',
		'emp_id':104,
		'email':'sk@gmail.com',
		'post':'Billing Executive'
		}

	json_data=json.dumps(data)
	r=requests.post(url=URL , data= json_data)
	data=r.json()
	print(data)

# post_data()
# Update Data
def update_data():
	data= {
		'id': 5 ,
		'name':'Shalika',
		'emp_id':105,
		'post':'Manager'
		}
	json_data=json.dumps(data)
	r=requests.put(url=URL , data= json_data)
	data=r.json()
	print(data)
# update_data()

def delete_data():
	data= {
		'id': 2 
		}
	json_data=json.dumps(data)
	r=requests.delete(url=URL , data= json_data)
	data=r.json()
	print(data)
delete_data()
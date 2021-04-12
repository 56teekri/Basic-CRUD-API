import requests
import json

def get_data(id=None):
    data={}
    if(id is not None):
        data={'id':id}
    json_data=json.dumps(data)
    headers={'Content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data) 
#URL="http://127.0.0.1:8000/getdata"
#get_data()

def create_data():
    data={
        'name':'laala',
        'roll':6,
        'city':'mathura'
    }
    headers={'Content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
#URL="http://127.0.0.1:8000/createdata"
#create_data()

def update_data():
    data={
        'id':8,
        'name':'chiti maharaj'
    }
    json_data=json.dumps(data)
    headers={'Content-Type':'application/json'}
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
#URL="http://127.0.0.1:8000/updatedata"
#update_data()

def delete_data():
    data={
        'id':10
    }
    json_data=json.dumps(data)
    headers={'Content-Type':'application/json'}
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
#URL="http://127.0.0.1:8000/deletedata"
#delete_data()

import requests
import json


def get_data(id=None):
    data={}
    if(id is not None):
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    if('json' in r.headers.get('Content-Type')):
        data=r.json()
    else:
        print("Response is not in JSON format")
        data="spam"
    print(data)

#URL="http://127.0.0.1:8000/getdata"
#get_data()



def create_data():
    data={
        'name':'chitti',
        'roll':7,
        'city':'mathura'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    if('json' in r.headers.get('Content-Type')):
        data=r.json()
    else:
        print("Response is not in JSON format")
        data="spam"
    print(data)

URL="http://127.0.0.1:8000/createdata"
create_data()



def update_data():
    data={
        'id':5,
        'city':'mathura'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    if('json' in r.headers.get('Content-Type')):
        data=r.json()
    else:
        print("Response is not in JSON format")
        data="spam"
    print(data)

#URL="http://127.0.0.1:8000/updatedata"
#update_data()

def delete_data():
    data={
        'id':6
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    if('json' in r.headers.get('Content-Type')):
        data=r.json()
    else:
        print("Response is not in JSON format")
        data="spam"
    print(data)

#URL="http://127.0.0.1:8000/deletedata"
#delete_data()

#!/usr/bin/env python
# Silvano Chitoca
# Site:http://www.silvanochitoca.org
# Github:SilvanoChitocaDB7
# Email: silvanochtioca@protonmail.com
import json
import requests

url = "https://api.useombala.ao/v1/messages"
data = {"message":"Bom dia Pedro","from":"924680610","to":"922105830"}
token = 'c570185f-ac81-4da1-a03f-85e85d5c8656'
headers ={'Authorization':f'Token {token}','Content-Type': 'application/json'}
response=requests.post(url,headers=headers,data=json.dumps(data))
print(response.text)
print(response.status_code)

#url2 = "https://api.useombala.ao/v1/messages"
#headers2 ={'Authorization':f'Token {token}'}
#params2={'page':0}
#response2=requests.get(url2,headers=headers2,params=params2)
#print(response2.text)
#print(response2.status_code)

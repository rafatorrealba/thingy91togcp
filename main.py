import json
import requests
import google.cloud
import firebase_admin
from firebase_admin import credentials, firestore

def main(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        query_write()
        return f'Basde de datos actualizada'
    elif request_json and 'message' in request_json:
        query_write()
        return f'Basde de datos actualizada'
    else:
        query_write()
        return f'Basde de datos actualizada'

def query_write():
    cred = credentials.Certificate("key.json")
    firebase_admin.initialize_app(cred)

    url = "https://api.nrfcloud.com/v1/messages"
    headers = {"Authorization":"Bearer 7f6ce6e19498f1fddfa28b49a8b05405ac5b409c"}

    req = json.loads(requests.get(url, headers=headers).text)
    msg = {"ID" : req["items"][0]["deviceId"], "DATE" : req["items"][0]["receivedAt"][0:10], "TIME" : req["items"][0]["receivedAt"][11:-1]}

    num = 0
    while num < len(req["items"]):
        if req["items"][num]["message"]["appId"] == "TEMP":
            msg.update({"TEMP" : req["items"][num]["message"]["data"]})
        elif req["items"][num]["message"]["appId"] == "HUMID":
            msg.update({"HUMID" : req["items"][num]["message"]["data"]})
        elif req["items"][num]["message"]["appId"] == "AIR_PRESS":
            msg.update({"AIR_P" : req["items"][num]["message"]["data"]})
        num += 1

    store = firestore.client()
    doc_ref = store.collection('thingy91')
    doc_ref.add(msg)

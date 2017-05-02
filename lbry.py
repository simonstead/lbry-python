import requests
import json

base_url = "http://127.0.0.1:5279/lbryapi/"

def _request(method_name, body={}):
    payload = { "method": method_name }
    if body != {}:
        payload.body = body
    r = requests.post(base_url, data=json.dumps(payload))
    return r

def channel_list_mine():
    method_name = "channel_list_mine"
    return _request(method_name)

def claim_list_mine():
    method_name = "claim_list_mine"
    return _request(method_name)

def wallet_balance():
    method_name = "wallet_balance"
    return _request(method_name)

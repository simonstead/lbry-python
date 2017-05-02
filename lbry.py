import requests

base_url = "http://127.0.0.1:5279/lbryapi/"

def get():
  url = base_url + "get"
  return requests.get(url)

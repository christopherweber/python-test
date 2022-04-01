import requests
import json

webhook_url="http://127.0.0.1:2000/webhook"

data = {
    "name":"chris"
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-type':'application/json'})


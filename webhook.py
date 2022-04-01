import requests
import json

webhook_url="https://fh-demo.com/server.py/webhook"

data = {
    "name":"chris"
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-type':'application/json'})


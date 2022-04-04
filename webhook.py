import requests
import json

webhook_url="https://b8a2a272a2a6.ngrok.io/webhook"
webhook_url2="https://fh-demo.com/webhook"

data = {
    "name":"chris"
}

r = requests.post(webhook_url2, data=json.dumps(data), headers={'Content-type':'application/json'})


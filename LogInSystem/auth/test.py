from flask.json import jsonify
import requests

BASE = "http://127.0.0.1:5000/"

email = "jonasbullinkel8@gmail.com"
passwd = "pass1234"


response = requests.post(BASE + "/login", {"email": email, "password": passwd})
print (response.json())
if response.json()['message']:
    response = requests.get(BASE+ "/profile")
print (response.json())
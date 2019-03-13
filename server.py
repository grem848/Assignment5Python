from flask import Flask, request
import json

app = Flask(__name__)

SERVER_PASSWORD = '0Z'

@app.route('/', methods=['POST'])
def funct():
    data = request.get_data()
    my_dict = json.loads(data)
    CLIENT_PASSWORD = my_dict['password']
    if CLIENT_PASSWORD == SERVER_PASSWORD:
        response = app.response_class(status=200)
    else:
        response = app.response_class(status=403)
    return response
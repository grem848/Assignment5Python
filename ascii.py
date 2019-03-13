import string
import requests
import json

letters_and_numbers = list(string.ascii_letters)+list(string.digits)

string_list = []

for ln1 in letters_and_numbers:
    for ln2 in letters_and_numbers:
        string_list.append(str(ln1+ln2))

url = "http://localhost:5000/"

def call_server(password):
    jsonstr = json.dumps({ 'password' : password })
    r = requests.post(url, data=jsonstr)
    if r.status_code == 200:
        print('success')
        return password
    else:
        return ''    

right_pw = ''
for password in string_list[:5]:
    right_pw = call_server(password)
    if right_pw != '':
        break
        
print(right_pw)
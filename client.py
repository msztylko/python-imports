import requests

url = '127.0.0.1:5000/source'

r = requests.get(f'http://{url}')

print(r.text)

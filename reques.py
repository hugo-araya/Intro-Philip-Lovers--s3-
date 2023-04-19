import requests
x = requests.get('http://www.ucm.cl')
print(x.text)
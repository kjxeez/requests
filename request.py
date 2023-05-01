import json

import requests

url = 'https://httpbin.org/get'
params = {'fname': 'Isabella', 'lname': 'Akopyan'}
headers = {'Accept': 'application/json'}

response = requests.get(url, params=params, headers=headers)
print('1. Содержимое GET запроса:\n')
print(response.text)
print('Только заголовок:\n')
print(response.request.headers)
url2 = 'https://httpbin.org/post'
headers2 = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'fname': 'Isabella', 'lname': 'Akopyan', 'stdnum' : '1032203961'}
response2 = requests.post(url2, data=data, headers=headers2)
print('2. Содержимое POST запроса:\n')

print(f'Первая строка: {response2.request.method, response2.request.url} HTTP/{response2.raw.version}\n{response2.status_code, response2.reason}')
print(f'Заголовок: {response2.headers}')
print(f'Тело: {response2.text}')

url3 = 'https://httpbin.org/post'
headers3 = {'Content-Type': 'application/json'}
data = {'fname': 'Isabella', 'lname': 'Akopyan', 'stdnum' : '1032203961'}
json_data = json.dumps(data) # преобразуем словарь в формат JSON
response3 = requests.post(url3, data=json_data, headers=headers3)
print('3. Содержимое POST запроса:\n')


print(f'Тело: {response3.text}')

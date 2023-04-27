import requests

url = 'https://httpbin.org/get'
params = {'fname': 'Isabella', 'lname': 'Akopyan'}
headers = {'Accept': 'application/json'}

response = requests.get(url, params=params, headers=headers)
# print('Содержимое GET запроса:\n')
# print(response.text)
# print('Только заголовок:\n')
# print(response.request.headers)
url2 = 'https://httpbin.org/post'
headers2 = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'fname': 'Isabella', 'lname': 'Akopyan', 'stdnum' : '1032203961'}
response2 = requests.post(url2, data=data, headers=headers2)
print('Содержимое POST запроса:\n')

print(f'Первая строка: {response2.status_code, response2.reason}')
print(f'Заголовок: {response2.headers}')
print(f'Тело: {response2.text}')

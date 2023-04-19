import requests

# Создание вызова API и сохранение ответа.
url = 'htts://api,github.com/search/repositiries?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Statuse code: {r.status_code}')

# Сохранение ответа API в переменной.
response_dict = r.json()

# Обработка результатов.
print(response_dict.keys())

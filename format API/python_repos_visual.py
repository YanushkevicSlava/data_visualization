import requests
from plotly.graph_objs import Bar
from plotly import offline


# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Statuse code: {r.status_code}')

# Обработка результатов.
response_dict = r.json()
repo_dicts = response_dict['items']
pero_names, stars = [], []
for repo_dict in repo_dicts:
    pero_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Построение визуализации.
data = [{
    'type': 'bar',
    'x': pero_names,
    'y': stars,
}]
my_layout = {
    'title': 'MostStarred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

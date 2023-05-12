import requests

from plotly.graph_objs import Bar
from plotly import offline

#Wykonanie wywoałania API i zahcowanie otrzymanej odpowiedzi.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

#Umieszczenie odpowiedzi API w zmiennej.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
	repo_names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#Utworzenie wizualizacji.
data = [{
	'type': 'bar',
	'x': repo_names,
	'y': stars,
}]

my_layout = {
	'title': 'Oznaczone największą liczbą gwiazdek projekty Pythona w serwisie GitHub',
	'xaxis': {'title': 'Repozytorium'},
	'yaxis': {'title': 'Gwiazdki'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline

import requests

#Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

#Przetworzenie informacji o każdym artykule.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	#Przygotowanie oddzielnego wywołania API dla każdego artykułu
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	reponse_dict = r.json()

	#Utworzenie słownika dla każdego artykułu.
	submission_dict = {
		'title': reponse_dict['title'],
		'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
		'comments': reponse_dict.get('descendants', 0),
	}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
							reverse=True)

title_links, comments, hn_links = [], [], []
for submission_dict in submission_dicts:
	title = submission_dict['title']
	hn_link = submission_dict['hn_link']
	title_link = f"<a href='{hn_link}'>{title}</a>"

	hn_links.append(hn_link)
	title_links.append(title_link)

	comment = submission_dict['comments']
	
	if comment < 10:
		continue
	else:
		comments.append(comment)

data = [{
	'type': 'bar',
	'x': title_links,
	'y': comments,
	'hovertext': hn_links,
	'marker': {
			'color': 'rgb(60, 100, 150)',
			'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6
}]

my_layout = {
	'title': 'Najbardziej aktywne dyskusje w serwisie Hacker News',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Tytuł artykułu',
		'titlefont': {'size':24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Ilość Komentarzy',
		'titlefont': {'size':24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_visual.html')
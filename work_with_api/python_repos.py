import requests

#Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")
#Umieszczenie odpowiedzi API w zmiennej.
response_dict = r.json()
print(f"Całkowita liczba repozytoriów: {response_dict['total_count']}")

#Przetworzenie informacji o repozytoriach.
repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytoriów: {len(repo_dicts)}")

print('\nWybrane informacje o każdym repozytorum:')

for repo_dict in repo_dicts:
	print(f"\nNazwa: {repo_dict['name']}")
	print(f"Właściciel: {repo_dict['owner']['login']}")
	print(f"Gwiazdkii: {repo_dict['stargazers_count']}")
	print(f"Repozytorium: {repo_dict['html_url']}")
	print(f"Opis: {repo_dict['description']}")
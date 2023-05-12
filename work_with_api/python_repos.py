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

#Przeanalizowanie pierwszego repozytorium.
repo_dict = repo_dicts[0]
print(f"\nKlucze: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
	print(key)
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

print('\nWybrane informacje o pierwszym repozytorum:')
print(f"Nazwa: {repo_dict['name']}")
print(f"Właściciel: {repo_dict['owner']['login']}")
print(f"Gwiazdkii: {repo_dict['stargazers_count']}")
print(f"Repozytorium: {repo_dict['html_url']}")
print(f"Utworzone: {repo_dict['created_at']}")
print(f"Uaktualnione: {repo_dict['updated_at']}")
print(f"Opis: {repo_dict['description']}")
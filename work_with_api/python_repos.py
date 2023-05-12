import requests

#Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")
#Umieszczenie odpowiedzi API w zmiennej.
response_dict = r.json()

#Przetworzenie wyników
print(response_dict.keys())
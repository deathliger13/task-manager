import requests


response = requests.get('https://api.github.com/user', auth=('deathliger666', 'oleg13081995'))
print(response.status_code)

print(response.json())
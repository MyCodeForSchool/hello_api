import requests

# data = requests.get('https://catfact.ninja/fact').json()
# print(data)
# fact = data['fact']
# print(f'A random cat fact is: {fact}')

try:
    response = requests.get('https://catfact.ninja/fact')
    print(response.status_code)
    response.raise_for_status()#raise exception for 400 or 500 status code
    print(response.text)
    print(response.json())

    data = response.json()
    fact = data['fact']
    print(f'A random cat fact is: {fact}')
except Exception as e:
    print(e)
    print('There was an error making this request.')







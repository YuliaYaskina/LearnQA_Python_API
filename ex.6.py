import requests
response = requests.get("https://playground.learnqa.ru/api/long_redirect")
for first_response in response.history:
    print(first_response.url)
last_response = response
print(last_response.url)
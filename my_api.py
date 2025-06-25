import requests

api_key  = "e3c0d09979ad476686ca082aadf6706c"

url    = "https://api.spoonacular.com/recipes/complexSearch"

params = {
    "apiKey":   api_key,
}


response = requests.get(url, params=params)
print("Status code:", response.status_code)


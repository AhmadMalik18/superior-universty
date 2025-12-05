import requests
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Could not retrieve joke"}
    
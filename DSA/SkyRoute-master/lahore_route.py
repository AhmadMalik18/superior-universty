import requests

API_KEY = "5b3ce3597851110001cf62487bd788f9c9f94a02b18fc2730e433f78"  

def get_coordinates(address):
    url = "https://api.openrouteservice.org/geocode/search"
    params = {
        "api_key": API_KEY,
        "text": address,
        "boundary.country": "PK"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if not data['features']:
        print(f"Location not found: {address}")
        return None
    coords = data['features'][0]['geometry']['coordinates']
    return coords 
def get_route(start_address, end_address):
    start_coords = get_coordinates(start_address)
    end_coords = get_coordinates(end_address)
    if not start_coords or not end_coords:
        print("Could not find one or both locations. Please try again.")
        return
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "coordinates": [start_coords, end_coords]
    }
    response = requests.post(url, json=body, headers=headers)
    data = response.json()
    try:
        segment = data['features'][0]['properties']['segments'][0]
        distance = segment['distance'] / 1000  
        duration = segment['duration'] / 60 
        steps = segment['steps']
        print(f"Total distance: {distance:.2f} km")
        print(f"Average time to travel: {duration:.2f} minutes")
        print("Route steps:")
        for step in steps:
            print(f"- {step['instruction']}")
    except (KeyError, IndexError):
        print("Could not retrieve route. Please check your locations and try again.")

get_route("Liberty Market, Lahore", "Badshahi Mosque, Lahore")
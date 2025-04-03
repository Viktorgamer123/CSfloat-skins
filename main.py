import requests
import json

# Definieer het API-eindpunt
api_url = "https://my-json-server.typicode.com/Viktorgamer123/CSfloat-skins/db"

# Maak een GET-aanroep naar de API
response = requests.get(api_url)

# Controleer of de aanroep succesvol was
if response.status_code == 200:
    # Parseer de JSON-reactie
    data = response.json()
    
    # Functie om de data op een geformatteerde manier af te drukken
    def print_formatted_data(data):
        for category, items in data.items():
            print(f"\n{category}:")
            for item in items:
                for key, value in item.items():
                    print(f"  {key}: {value}")
                print()

    # Print de geformatteerde data
    print_formatted_data(data)
else:
    print(f"Het ophalen van data is mislukt: {response.status_code}")
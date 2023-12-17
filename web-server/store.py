import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text)) # es un string
    categories = r.json()# el formato json automáticamente me lo va a convertir rn una lista y los elementos de adentro van a ser diccionarios
    for category in categories:
        print(category['name'])


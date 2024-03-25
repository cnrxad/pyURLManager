import requests
from colors import *


def expand_url(short_url):
    try:
        response = requests.get(short_url)
        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            return response.url
        else:
            return "Error: La solicitud no fue exitosa."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == "__main__":
    short_url = input(f"{GREEN}Ingresa la URL acortada: {RESET}")
    expanded_url = expand_url(short_url)
    print(f"URL expandida: {expanded_url}")

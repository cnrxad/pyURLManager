from pyshorteners import Shortener
from colors import *


def shorten_url(original_url):
    shortener = Shortener()
    shortened_url = shortener.tinyurl.short(original_url)
    return shortened_url


# Solicitar al usuario que ingrese la URL original
original_url = input(f"{GREEN}Inserta la URL que deseas acortar:{RESET} https://")

# Acortar la URL ingresada por el usuario
shortened_url = shorten_url(original_url)

# Mostrar la URL acortada al usuario
print(f"La URL acortada es: {shortened_url}")

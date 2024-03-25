import os
from colors import *

os.system("cls")

print(
    f"""{BLUE}                               _                            
  ___ _ __  _ ____  ____ _  __| |                           
 / __| '_ \| '__\ \/ / _` |/ _` |                           
| (__| | | | |   >  < (_| | (_| |                           
 \___|_| |_|_|  /_/\_\__,_|\__,_|                           
 _   _ ____  _     __  __                                   
| | | |  _ \| |   |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
| | | | |_) | |   | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_| |  _ <| |___| |  | | (_| | | | | (_| | (_| |  __/ |   
 \___/|_| \_\_____|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                            |___/           {RESET}"""
)

print(
    """Servicios de gestión de URLs disponibles:
        1: URL shortener
        2: URL expander
    """
)


# Lista de scripts
scripts = ["shortener.py", "expander.py"]

# Leer el número del teclado alfanumérico
num = input(f"{YELLOW}¿Qué servicio deseas utilizar?: ")

# Buscar el script correspondiente al número introducido
try:
    num = int(num)
    if num < 1 or num > 2:
        raise ValueError("El número introducido no es válido.")
    script = scripts[
        num - 1
    ]  # Corregido para que coincida con el índice correcto de la lista
except (
    ValueError,
    IndexError,
) as e:  # Añadido IndexError para manejar errores de índice fuera de rango
    print(f"Error: {e}")
    exit()

# Ejecutar el script correspondiente
try:
    os.system(f"python {script}")
except Exception as e:
    print(f"Error al ejecutar el script: {e}")

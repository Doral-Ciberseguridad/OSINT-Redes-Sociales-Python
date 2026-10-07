# Importo librerias necesarias
import requests as requests  # Librería para las solicitudes
import time  # Librería para tiempo de espera en la consola
from colorama import Fore  # Librería para el tipo de color de la salida en la consola
import webbrowser  # Para abrir páginas web
import whois  # Para obtener información de las páginas web

# Mensaje Bienvenida
time.sleep(2)
print("\n\nBienvenido al programa")
print("En este programa investigaremos a usuarios en las redes sociales\n")

usuario = input("Dime el nombre del usuario que deseas investigar --->")
print("\n")
time.sleep(2)

# Muestro al usuario las opciones para elegir
print(f"Elige una de estas opciones para investigar al usuario \"{usuario}\":")
print("\n")
time.sleep(2)
print(Fore.MAGENTA + "1.Investigar en Instagram")
print(Fore.RED + "2.Investigar en Youtube")
print(Fore.BLACK + "3.Investigar en Tiktok")
print(Fore.YELLOW + "4.Investigar en Facebook")
print(Fore.BLUE + "5.Investigar en Discord")
print(Fore.WHITE + "6.Investigar en todas las anteriores")
print("\n")
time.sleep(2)
opcion_usuario = int(input("Elige --->"))

# Decoración
print("\nBuscando...")
time.sleep(1)
print("[---25%---]")
time.sleep(1)
print("[---50%---]")
time.sleep(1)
print("[---75%---]")
time.sleep(1)
print("[---100%---]\n")
time.sleep(1)

# Lista para almacenar las URLs de las plataformas donde se encontró al usuario
plataformas_para_whois = []

# Funciones para buscar el usuario en las plataformas

# Función para Instagram
def instagram():
    url_instagram2 = f"https://www.instagram.com/{usuario}"
    respuesta_instagram = requests.get(url_instagram2)
    if respuesta_instagram.status_code == 200:
        print(Fore.MAGENTA + "Se encontró al usuario en Instagram")
        time.sleep(2)
        print(f"En breve se abrirá el enlace: {url_instagram2}\n")
        time.sleep(5)
        webbrowser.open(url_instagram2)
        plataformas_para_whois.append(url_instagram2)
    else:
        print(Fore.MAGENTA + "No se encontró al usuario en Instagram\n")
        time.sleep(2)

# Función para YouTube
def youtube():
    url_youtube2 = f"https://www.youtube.com/{usuario}"
    respuesta_youtube = requests.get(url_youtube2)
    if respuesta_youtube.status_code == 200:
        print(Fore.RED + "Se encontró al usuario en YouTube")
        time.sleep(2)
        print(f"En breve se abrirá el enlace: {url_youtube2}\n")
        time.sleep(5)
        webbrowser.open(url_youtube2)
        plataformas_para_whois.append(url_youtube2)
    else:
        print(Fore.RED + "No se encontró al usuario en YouTube\n")
        time.sleep(2)

# Función para TikTok
def tiktok():
    url_tiktok2 = f"https://www.tiktok.com/@{usuario}"  # Cambio en la estructura de la URL
    respuesta_tiktok = requests.get(url_tiktok2)
    if respuesta_tiktok.status_code == 200:
        print(Fore.BLACK + "Se encontró al usuario en TikTok")
        time.sleep(2)
        print(f"En breve se abrirá el enlace: {url_tiktok2}\n")
        time.sleep(5)
        webbrowser.open(url_tiktok2)
        plataformas_para_whois.append(url_tiktok2)
    else:
        print(Fore.BLACK + "No se encontró al usuario en TikTok\n")
        time.sleep(2)

# Función para Facebook
def facebook():
    url_facebook2 = f"https://www.facebook.com/{usuario}"
    respuesta_facebook = requests.get(url_facebook2)
    if respuesta_facebook.status_code == 200:
        print(Fore.YELLOW + "Se encontró al usuario en Facebook")
        time.sleep(2)
        print(f"En breve se abrirá el enlace: {url_facebook2}\n")
        time.sleep(5)
        webbrowser.open(url_facebook2)
        plataformas_para_whois.append(url_facebook2)
    else:
        print(Fore.YELLOW + "No se encontró al usuario en Facebook\n")
        time.sleep(2)

# Función para Discord
def discord():
    url_discord2 = f"https://discord.com/{usuario}"
    respuesta_discord = requests.get(url_discord2)
    if respuesta_discord.status_code == 200:
        print(Fore.BLUE + "Se encontró al usuario en Discord")
        time.sleep(2)
        print(f"En breve se abrirá el enlace: {url_discord2}\n")
        time.sleep(5)
        webbrowser.open(url_discord2)
        plataformas_para_whois.append(url_discord2)
    else:
        print(Fore.BLUE + "No se encontró al usuario en Discord\n")
        time.sleep(2)

# Ejecuto la función que haya elegido el usuario
if opcion_usuario == 1:
    instagram()
elif opcion_usuario == 2:
    youtube()
elif opcion_usuario == 3:
    tiktok()
elif opcion_usuario == 4:
    facebook()
elif opcion_usuario == 5:
    discord()
elif opcion_usuario == 6:
    instagram()
    youtube()
    tiktok()
    facebook()
    discord()
else:
    print("\nEsa no es una opción válida, tienes que meter un número del 1 al 6\n")
    time.sleep(2)

# Pregunto al usuario si quiere buscar en un nuevo sitio
print("")
time.sleep(2)
print(Fore.WHITE + "¿Hay algún sitio más sobre el que quieras investigar? (SI/NO)\n")
time.sleep(2)
respuesta = input("--->")

# Busco en ese nuevo sitio
if respuesta.lower() == "si":
    print("\nMuy bien, indica el sitio.com en el que quieres buscar:")
    sitio_nuevo = input("--->")
    print("\n")
    time.sleep(2)
    url_nueva = f"https://{sitio_nuevo}/{usuario}"
    respuesta_nueva = requests.get(url_nueva)
    if respuesta_nueva.status_code == 200:
        print(f"Se encontró al usuario en {sitio_nuevo}")
        time.sleep(2)
        print(f"Pronto se abrirá el enlace: {url_nueva}\n")
        time.sleep(5)
        webbrowser.open(url_nueva)
        plataformas_para_whois.append(url_nueva)
    else:
        print(f"No se pudo encontrar a {usuario} en {sitio_nuevo}\n")
        time.sleep(2)
else:
    print(Fore.WHITE + "Esta bien no pasa nada...\n")
    time.sleep(2)

# Muestro los sitios exitosos
time.sleep(2)
print(Fore.WHITE + "")
print(f"Estas son los sitios en los que se ha encontrado a {usuario}:")
for plataforma in plataformas_para_whois:
    print(plataforma)

# Genero un informe detallado con WHOIS
print("\n")
print("¿Deseas un informe más detallado sobre estos sitios? (SI/NO)")
respuesta2 = input("--->")
# Decoración
print("\nGenerando informe...")
time.sleep(1)
print("[---25%---]")
time.sleep(1)
print("[---50%---]")
time.sleep(1)
print("[---75%---]")
time.sleep(1)
print("[---100%---]\n")
time.sleep(1)
informe_final = ""  # Inicio el informe

if respuesta2.lower() == "si":
    for plataforma in plataformas_para_whois:
        dominio = plataforma.split("//")[1]  # Extraer el dominio de la URL
        informe_plataforma = whois.whois(dominio)
        informe_final += str(informe_plataforma) + "\n\n"
        print("\n")
else:
    print("Está bien, no pasa nada...")

# Pregunto al usuario si quiere ver el informe
print("¿Deseas ver el informe? (SI/NO)")
respuesta3 = input("--->")
if respuesta3.lower() == "si":
    print("Aquí tienes el informe:")
    print("\n")
    print(informe_final)

# M
print("Gracias por usar el programa!!!\n")
time.sleep(2)


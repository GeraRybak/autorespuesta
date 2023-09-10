# https://my.telegram.org/apps para crear la app con el numero de telefono de 
# Bajar python de https://www.python.org
# Se instala la libreria con el comando "pip instal telethon" desde la consola de powershell
# Se utiliza el bot @RawDataBot para obtener el Id de telegram

import time
from telethon import TelegramClient, events

# Ahi van los datos de la pagina https://my.telegram.org/apps
api_id = 123456
api_hash = '123445ansdjasdgja'

# Tu ID de usuario de Telegram
mi_id = 12345678  # Reemplaza con tu propio ID

# Crear el cliente de Telegram
client = TelegramClient('user', api_id, api_hash)

# Un diccionario para mantener el registro de la última respuesta para cada usuario
last_response_time = {}

@client.on(events.NewMessage)
async def handler(event):
    message = event.message
    sender = await message.get_sender()

    # Verificar si el mensaje proviene de un usuario (no de un grupo o canal)
    if sender.id != mi_id:
        user_id = sender.id

        # Obtener la hora actual
        current_time = time.time()

        # Verificar si ya hemos respondido en los últimos 15 minutos (900 segundos)
        if user_id not in last_response_time or current_time - last_response_time[user_id] >= 900:
            # Responder al mensaje
            await message.reply("Hola, buenos días. ¿En qué podemos ayudarte? Favor brindarnos el número de teléfono y los últimos 4 dígitos de la serie de la ONT.")
            
            # Registrar la hora de la última respuesta
            last_response_time[user_id] = current_time

# Iniciar el cliente
with client:
    # Esperar eventos hasta que se desconecte
    client.run_until_disconnected()

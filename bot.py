import sys
import glob
import importlib
from pathlib import Path
import logging
import logging.config
import asyncio
import pytz
from datetime import date, datetime
from aiohttp import web

from pyrogram import idle
# Importaciones de configuración del bot
from config import LOG_CHANNEL, ON_HEROKU, PORT
# Importación de las cadenas de texto del bot
from Script import script
# Importaciones del servidor web de streaming
from TechVJ.server import web_server
# Importaciones del cliente principal del bot y utilidades de streaming
from TechVJ.bot import StreamBot
from TechVJ.utils.keepalive import ping_server
from TechVJ.bot.clients import initialize_clients

# --- Configuración de Logging ---
# Carga la configuración de logging desde el archivo 'logging.conf'
logging.config.fileConfig('logging.conf')
# Establece el nivel de logging global a INFO
logging.getLogger().setLevel(logging.INFO)
# Establece el nivel de logging para la biblioteca Pyrogram a ERROR para reducir el ruido en los logs
logging.getLogger("pyrogram").setLevel(logging.ERROR)

# Inicia la instancia principal del bot StreamBot (definida en TechVJ/bot/__init__.py)
StreamBot.start()
# Obtiene el bucle de eventos predeterminado de asyncio
loop = asyncio.get_event_loop()

async def start_services():
    """
    Función principal asíncrona para iniciar y gestionar todos los servicios del bot.
    Esto incluye:
    - Inicializar el bot principal y obtener su nombre de usuario.
    - Inicializar clientes adicionales para streaming (si configurado).
    - Cargar dinámicamente todos los plugins desde el directorio 'plugins'.
    - Iniciar un servidor web para manejar solicitudes de stream/descarga.
    - Enviar un mensaje de notificación de reinicio al canal de logs.
    - Mantener el bot en ejecución.
    """
    print('\nIniciando Bot de Almacenamiento de Archivos...')

    # Obtener información del bot y establecer su nombre de usuario
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username

    # Inicializar clientes adicionales para streaming (si la configuración lo permite)
    await initialize_clients()

    # Cargar todos los plugins dinámicamente desde la carpeta 'plugins'
    plugins_path = "plugins/*.py"
    plugin_files = glob.glob(plugins_path) # Busca todos los archivos .py en la carpeta plugins
    for file_path in plugin_files:
        # Extraer el nombre del plugin del nombre del archivo (ej. 'commands' de 'commands.py')
        plugin_name = Path(file_path).stem.replace(".py", "")
        plugins_dir = Path(f"plugins/{plugin_name}.py") # Ruta completa al archivo del plugin
        
        # Importar el módulo del plugin usando importlib
        import_path = f"plugins.{plugin_name}"
        spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
        loaded_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(loaded_module)
        sys.modules[import_path] = loaded_module # Agrega el módulo cargado a sys.modules
        print(f"Plugin cargado: {plugin_name}")

    # Si la variable de entorno ON_HEROKU es True, inicia la tarea de ping para mantener el servidor activo
    if ON_HEROKU:
        asyncio.create_task(ping_server())

    # Iniciar el servidor web (para manejar solicitudes de stream y descarga directa)
    web_app_runner = web.AppRunner(await web_server())
    await web_app_runner.setup() # Configura la aplicación web
    bind_address = "0.0.0.0" # El servidor escuchará en todas las interfaces de red disponibles
    await web.TCPSite(web_app_runner, bind_address, PORT).start() # Inicia el servidor HTTP

    # Enviar un mensaje de notificación de reinicio al canal de logs
    timezone_kolkata = pytz.timezone('Asia/Kolkata') # Define la zona horaria
    current_date = date.today() # Obtiene la fecha actual
    current_time = datetime.now(timezone_kolkata).strftime("%H:%M:%S %p") # Obtiene la hora actual formateada
    await StreamBot.send_message(
        chat_id=LOG_CHANNEL,
        text=script.RESTART_TXT.format(current_date, current_time)
    )

    print("✅ Bot iniciado exitosamente.")
    # Mantiene el bot en ejecución indefinidamente hasta que se detenga manualmente (ej. Ctrl+C)
    await idle()

# Punto de entrada principal para la ejecución del script
if __name__ == '__main__':
    try:
        # Ejecuta la función 'start_services' hasta que se complete
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        # Maneja la interrupción por teclado (Ctrl+C)
        logging.info('Servicio detenido por el usuario. ¡Adiós! 👋')
    except Exception as e:
        # Captura cualquier otra excepción fatal al inicio y la registra
        logging.critical(f"Error fatal al iniciar el bot: {e}", exc_info=True)

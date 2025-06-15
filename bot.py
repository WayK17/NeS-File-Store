# bot.py

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

# Configuraciones de logging
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

from pyrogram import Client, idle
from config import LOG_CHANNEL, ON_HEROKU, PORT
from Script import script
from TechVJ.server import web_server
from TechVJ.bot import StreamBot
from TechVJ.utils.keepalive import ping_server
from TechVJ.bot.clients import initialize_clients

# Iniciar el bot principal
StreamBot.start()
loop = asyncio.get_event_loop()

async def start_services():
    print('\nInicializando Bot...')
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username
    
    # Cargar todos los plugins
    ppath = "plugins/*.py"
    files = glob.glob(ppath)
    for name in files:
        patt = Path(a.name)
        plugin_name = patt.stem
        import_path = f"plugins.{plugin_name}"
        spec = importlib.util.spec_from_file_location(import_path, f"plugins/{plugin_name}.py")
        load = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(load)
        sys.modules[import_path] = load
        print(f"Plugin importado => {plugin_name}")

    # Inicializar clientes adicionales si es necesario (para streaming)
    await initialize_clients()

    # Iniciar servidor web y ping si está en Heroku
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    
    # Mensaje de reinicio
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await StreamBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    
    print("✅ Bot iniciado exitosamente")
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logging.info('Servicio detenido.')

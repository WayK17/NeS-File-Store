import re
import os
from os import environ
from Script import script # Importa el módulo script para usar sus cadenas de texto

# Patrón para identificar IDs numéricos (usado para validar IDs de administradores)
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    """
    Convierte un valor de cadena (True, False, 1, 0, yes, no, etc.) a un booleano.
    Si el valor no es reconocido, devuelve el valor por defecto.
    """
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# --- Información del Bot ---
# API_ID: ID de la API de Telegram, obtenido de my.telegram.org
API_ID = int(environ.get("API_ID", "15353803"))
# API_HASH: Hash de la API de Telegram, obtenido de my.telegram.org
API_HASH = environ.get("API_HASH", "0dc88c619c52613806822fd600eec006")
# BOT_TOKEN: Token del bot, obtenido de BotFather
BOT_TOKEN = environ.get("BOT_TOKEN", "8112764734:AAG6_n42MvPY7OVhy2aheE_qc_84_XQo2MA")

# PICS: Lista de URLs de imágenes para usar en el mensaje de inicio del bot
PICS = (environ.get('PICS', 'https://iili.io/3Q8HbFs.jpg/IMG22052025.jpg')).split()
# ADMINS: Lista de IDs de usuario de administradores del bot
# Convierte los IDs a enteros si son numéricos
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6279723048').split()]
# BOT_USERNAME: Nombre de usuario del bot (sin el '@')
BOT_USERNAME = environ.get("BOT_USERNAME", "")
# PORT: Puerto para el servidor web (usado en plataformas como Heroku)
PORT = environ.get("PORT", "8080")

# --- Configuración de Base de Datos (MongoDB) ---
# DB_URI: URI de conexión a la base de datos MongoDB
DB_URI = environ.get("DB_URI", "mongodb+srv://WayK:m3olvidexD@nesscloud.oqcpd.mongodb.net")
# DB_NAME: Nombre de la base de datos
DB_NAME = environ.get("DB_NAME", "WayK")

# --- Configuración de Auto-Eliminación ---
# AUTO_DELETE_MODE: Habilita/deshabilita la eliminación automática de mensajes
AUTO_DELETE_MODE = is_enabled((environ.get('AUTO_DELETE_MODE', "True")), True)
# AUTO_DELETE: Tiempo en minutos antes de que un mensaje se elimine automáticamente (para el mensaje de advertencia)
AUTO_DELETE = int(environ.get("AUTO_DELETE", "10"))
# AUTO_DELETE_TIME: Tiempo en segundos antes de que un mensaje se elimine automáticamente (para el archivo real)
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "600"))

# --- Configuración de Canales ---
# LOG_CHANNEL: ID del canal de logs (debe empezar con -100)
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002514857367"))

# --- Configuración de Caption de Archivos ---
# CUSTOM_FILE_CAPTION: Caption personalizado para archivos individuales
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
# BATCH_FILE_CAPTION: Caption personalizado para archivos enviados en lotes (si no se define, usa CUSTOM_FILE_CAPTION)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# --- Configuración de Almacenamiento Público ---
# PUBLIC_FILE_STORE: Si es True, cualquier usuario puede usar el bot para almacenar archivos
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

# --- Configuración de Verificación (Shortlink) ---
# VERIFY_MODE: Habilita/deshabilita el modo de verificación mediante shortlinks
VERIFY_MODE = is_enabled((environ.get('VERIFY_MODE', "False")), False)
# SHORTLINK_URL: Dominio del servicio de acortamiento de enlaces (ej: "shrinkme.io", "api.shareus.io")
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
# SHORTLINK_API: Clave API de tu cuenta en el servicio de acortamiento de enlaces
SHORTLINK_API = environ.get("SHORTLINK_API", "")
# VERIFY_TUTORIAL: URL a un tutorial que explica cómo pasar la verificación
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")

# --- Configuración de URL de Sitio Web (para enlaces de descarga/stream directos) ---
# WEBSITE_URL_MODE: Habilita/deshabilita el uso de una URL de sitio web personalizada para los enlaces
WEBSITE_URL_MODE = is_enabled((environ.get('WEBSITE_URL_MODE', "False")), False)
# WEBSITE_URL: URL base de tu sitio web donde se alojarán los enlaces directos (ej: "https://midominio.com/")
WEBSITE_URL = environ.get("WEBSITE_URL", "")

# --- Configuración de Stream de Archivos ---
# STREAM_MODE: Habilita/deshabilita el modo de stream para archivos multimedia
STREAM_MODE = is_enabled((environ.get('STREAM_MODE', "False")), False)
# MULTI_CLIENT: Indica si se usan múltiples clientes para el streaming (manejo de carga)
MULTI_CLIENT = False # Esta variable está en TechVJ/bot/clients.py, se mantiene aquí por consistencia.
# SLEEP_THRESHOLD: Umbral de espera para Pyrogram (tiempo en segundos para dormir si la conexión está inactiva)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
# PING_INTERVAL: Intervalo en segundos para enviar pings al servidor y mantenerlo activo (ej. en Heroku)
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutos
# ON_HEROKU: Booleano que indica si la aplicación se está ejecutando en Heroku
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
# URL: URL base del bot para generar enlaces de stream/descarga directos
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")

# --- Configuración de Broadcast con Auto-Borrado ---
# BROADCAST_DELETE_DELAY: Tiempo en segundos que un mensaje de broadcast permanecerá visible antes de ser borrado automáticamente
BROADCAST_DELETE_DELAY = int(environ.get("BROADCAST_DELETE_DELAY", "3600"))

# --- Configuración de Suscripción Forzada ---
# FORCE_SUB_ENABLED: Habilita/deshabilita la suscripción forzada a un canal
FORCE_SUB_ENABLED = is_enabled(environ.get('FORCE_SUB_ENABLED', "True"), True)
# FORCE_SUB_CHANNEL: ID numérico o @username del canal al que deben unirse los usuarios
FORCE_SUB_CHANNEL = environ.get('FORCE_SUB_CHANNEL', "-1002661251789")
# FORCE_SUB_INVITE_LINK: Enlace de invitación al canal de suscripción forzada
FORCE_SUB_INVITE_LINK = environ.get('FORCE_SUB_INVITE_LINK', "https://t.me/+0mbRE6ULxftkZjNh")
# SKIP_FORCE_SUB_FOR_ADMINS: Si es True, los administradores del bot pueden saltar la suscripción forzada
SKIP_FORCE_SUB_FOR_ADMINS = is_enabled(environ.get('SKIP_FORCE_SUB_FOR_ADMINS', "True"), True)

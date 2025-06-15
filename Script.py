# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01


class script(object):
    START_TXT = """<b>¡Hola {} 👋!, Soy {}. Bienvenido a nuestro bot de almacenamiento de archivos.</b>""" # Ajustado para mencionar al bot en la bienvenida

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01


    CAPTION = """<b>📂 Archivo:</b> <code>{file_name}</code>

<b>⚙️ Tamaño:</b> <code>{file_size}</code>

<b>[「NESS Cloud」](https://t.me/Ness_Cloud)</b>"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

    SHORTENER_API_MESSAGE = """<b>Para agregar o actualizar tu API del Sitio Acortador: <code>/api (tu_api)</code>
            
<b>Ej: <code>/api 6LZq851sXofffPHugiKQq</code>

<b>Sitio Web Actual:</b> <code>{base_site}</code>

<b>API del Acortador Actual:</b> <code>{shortener_api}</code>

Si deseas eliminar la API, envía: <code>/api None</code>"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

    CLONE_START_TXT = """<b>¡Hola {} 👋! Mi nombre es {}. Soy un bot de almacenamiento de archivos avanzado y potente, con soporte de acortador de URL personalizado, función de auto-borrado y una interfaz de usuario mejorada.

Si quieres estas características, crea tu propio bot clon desde mi <a href="https://t.me/vj_botz">original</a>.</b>"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

    ABOUT_TXT = """<b>Hola, soy un Bot de Almacenamiento de Archivos Permanentes. 

🤖 Mi nombre: {me_mention}

📝 Lenguaje: <a href=https://www.python.org>Python3</a>

📚 Biblioteca: <a href=https://docs.pyrogram.org>Pyrogram</a>

🧑🏻‍💻 Desarrollador: <a href=https://t.me/WayK17X>WayK17</a>

👥 Grupo de Soporte: <a href=https://t.me/NESS_Soporte>NESS Soporte</a>

📢 Canal de Actualizaciones: <a href=https://t.me/NessCloud>Ness Cloud</a></b>
"""

    CABOUT_TXT = """<b>Hola, soy un Bot de Almacenamiento de Archivos Permanentes.

🤖 Mi nombre: {me_mention}

📝 Lenguaje: <a href=https://www.python.org>Python3</a>

📚 Biblioteca: <a href=https://docs.pyrogram.org>Pyrogram</a>

🧑🏻‍💻 Desarrollador: <a href=tg://user?id={}>Desarrollador</a></b>
"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

    CLONE_TXT = """<b>¡Hola {} 👋!

Primero envía el comando /clone y luego sigue estos pasos.
    
1) Envía <code>/newbot</code> a @BotFather
2) Asigna un nombre para tu bot.
3) Asigna un nombre de usuario único.
4) Luego recibirás un mensaje con tu token de bot.
5) Reenvía ese mensaje a mí.

Entonces intentaré crear una copia mía para ti solamente 😌</b>"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

    HELP_TXT = """<b><u>💢 CÓMO USAR EL BOT ☺️</u>

🔻 /start - Con este comando puedes verificar si el bot está activo.
🔻 /link - Responde a un video o archivo para obtener un enlace compartible.
🔻 /batch - Envía el enlace del primer post del canal de almacenamiento y luego el enlace del último post. Asegúrate de que el bot sea administrador en tu canal de almacenamiento.
   Ej: <code>/batch https://t.me/vj_botz/25 https://t.me/vj_botz/30</code>
🔻 /clone - Crea tu propio bot clon idéntico.
🔻 /base_site - Usa este comando para configurar el dominio de tu acortador de URLs.
   Ej: <code>/base_site tudominio.com</code>
🔻 /api - Configura la API de tu cuenta de acortador de URLs.
   Ej: <code>/api baowgwklaabakl</code>
🔻 /addpremium [ID] - Otorga acceso premium a un usuario (solo admins).
🔻 /addpremium [ID] [días] - Otorga acceso premium por `X` días a un usuario (solo admins).
🔻 /delpremium [ID] - Revoca el acceso premium de un usuario (solo admins).
🔻 /stats - Muestra estadísticas de usuarios (solo admins).
🔻 /deletecloned - Usa esto para eliminar tu bot clonado.
🔻 /broadcast - Responde a este comando con un mensaje para transmitirlo (solo para el propietario del bot).
🔻 /dbroadcast - Responde a este comando con un mensaje para transmitirlo y auto-borrarlo después de un tiempo (solo para el propietario del bot).
</b>"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

    CHELP_TXT = """<b>💢 Cómo Usar Este Bot ☺️

🔻 /start - Con este comando puedes verificar si el bot está activo.
🔻 /link - Responde a un video o archivo para obtener un enlace compartible.
🔻 /base_site - Usa este comando para configurar el dominio de tu acortador de URLs.
   Ej: <code>/base_site tudominio.com</code>
🔻 /api - Configura la API de tu cuenta de acortador de URLs.
   Ej: <code>/api baowgwklaabakl</code>
🔻 /broadcast - Responde a este comando con un mensaje para transmitirlo (solo para el propietario del bot).
</b>"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

    LOG_TEXT = """<b>👤 Nuevo Usuario</b>

ID: <code>{user_id}</code>  
Nombre: <b>{user_mention}</b>
"""
    RESTART_TXT = """
<b>🤖 ¡Bot Reiniciado!</b>

📅 <b>Fecha:</b> <code>{today}</code>  
⏰ <b>Hora:</b> <code>{time}</code>  
🌐 <b>Zona Horaria:</b> <code>Asia/Kolkata</code>  
🛠️ <b>Estado de Construcción:</b> <code>v2.7.1 [Estable]</code>"""


    # --- MENSAJE PARA FORZAR SUSCRIPCIÓN ---
    FORCE_MSG = """<b>🚧 Acceso Restringido 🚧</b>

<b>¡Hola {mention} 👋🏼!</b>

Para acceder a estos archivos, debes ser miembro del <b>CANAL</b>.

🔔 Una vez que te hayas unido, por favor, presiona el botón <b>'Intentar de Nuevo'</b>.

¡Gracias por tu apoyo! 🙌✨"""


    PREMIUM_REQUIRED_MSG = """<b>🚫 Acceso Restringido 🚫</b>

Hola {mention} 👋,
Lo sentimos, este enlace es exclusivo para usuarios <b>Premium</b> ✨.

<b>¿Quieres ser Premium?</b>
<blockquote>Escribe a nuestro bot para más información: <a href="https://t.me/NESS_SupporttBot">👉 Aquí 👈</a></blockquote>

<i>Gracias por tu interés y apoyo.</i> 💖
"""

# No Eliminar Crédito Tg - @VJ_Botz
# Suscríbete al Canal de YouTube Para Bots Increíbles https://youtube.com/@Tech_VJ
# Pregunta Dudas en telegram @KingVJ01

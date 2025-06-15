<p align="center">
  <img src="https://graph.org/file/d57d6f83abb6b8d0efb02.jpg" alt="VJ-FILE-STORE-BOT Logo">
</p>
<h1 align="center">
  BOT DE ALMACENAMIENTO DE ARCHIVOS VJ
</h1>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Bienvenido+al+BOT-DE-ALMACENAMIENTO-DE-ARCHIVOS-VJ;Un+Bot+Altamente+Avanzado+para+Almacenar+Archivos;Creado+Por+Yt-@Tech_VJ!;Con+Función+de+Clonación+y+Enlaces+de+Stream/Descarga;Acortador+de+URL+Personalizado+y+Función+de+Auto-Borrado;¡Un+Bot+Con+Funciones+Totalmente+Avanzadas!;¡Gracias!)
</p>

### Tutorial de Despliegue [Enlace al Video](https://youtu.be/VxAn9VcYtQg)

## Características

<b><details><summary>Toca aquí para ver las Características del Bot</summary>
 
- [x] Enlace Permanente a través del Sitio Web [Función Premium] 
- [x] Función de Clonación Añadida [Función Premium] 
- [x] Función de Verificación de Token 
- [x] Función de Stream Añadida con Soporte para Múltiples Reproductores
- [x] Soporte de Acortador de URL Personalizado (Cualquier usuario puede añadir su propio acortador)
- [x] Soporte de Lote Añadido (Cualquier usuario puede usar lotes haciendo al bot administrador en su canal de almacenamiento de archivos)
- [x] Función de Auto-Borrado Añadida
- [x] Mensaje de Inicio Personalizado con Imagen y Botones
</b>
</details>

## Variables de Entorno

<b><details><summary>Toca aquí para ver las Variables de Entorno</summary>

- `API_ID` : Obtener de [my.telegram.org](https://my.telegram.org)
- `API_HASH` : Obtener de [my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` : Obtener de [BotFather](https://telegram.me/BotFather)
- `BOT_USERNAME` : Tu nombre de usuario del Bot (sin @)
- `DB_URI` : URL de la base de datos de Mongodb para el Bot Principal [Ver Tutorial Aquí](https://youtu.be/DAHRmFdw99o)
- `CLONE_DB_URI` : URL de la base de datos de Mongodb para el Bot Clon [Ver Tutorial Aquí](https://youtu.be/DAHRmFdw99o)
- `ADMINS` : ID del Administrador/Propietario para Mensajes de Difusión.
- `LOG_CHANNEL` : ID del canal de registro (comienza con -100xxxxxx)
- `URL` : Enlace de tu Aplicación de Servidor con https:// y asegúrate de que termine con /.
- `AUTO_DELETE` : Tiempo en Minutos
- `AUTO_DELETE_TIME` : Tiempo en Segundos
- `PYTHON_VERSION` : Esta variable es solo para Render, el valor es `3.10.8`
- `PORT` : Esta variable es solo para Render, el valor es `8080`

- `VERIFY_MODE`: `True` o `False`. Habilita la verificación de enlaces.
- `SHORTLINK_URL`: Dominio del acortador (ej: `my.shortener.com`).
- `SHORTLINK_API`: Clave API de tu acortador.
- `VERIFY_TUTORIAL`: Enlace a un tutorial sobre cómo pasar la verificación.
- `FORCE_SUB_ENABLED`: `True` o `False`. Habilita la suscripción forzada.
- `FORCE_SUB_CHANNEL`: ID o username del canal de suscripción forzada (ej: `-1001234567890` o `@MiCanal`).
- `FORCE_SUB_INVITE_LINK`: Enlace de invitación al canal de suscripción forzada.
- `SKIP_FORCE_SUB_FOR_ADMINS`: `True` o `False`. Los administradores del bot pueden saltar la suscripción forzada.
</b>
</details>

## Ver Cómo se Ve el Bot

<b><details><summary>Toca aquí para ver la Demo del Bot</summary></b>

<img src="https://graph.org/file/bb9c59043c52072e8dc93.jpg" alt="Bot Demo">
<img src="https://graph.org/file/295e41dfab93acf42a111.jpg" alt="Bot Demo">
<img src="https://graph.org/file/ccc1b6ab4967a7d155ab8.jpg" alt="Bot Demo">
<img src="https://graph.org/file/75db5257c39436b734b49.jpg" alt="Bot Demo">
<img src="https://graph.org/file/1ce62a17012ed5723aaca.jpg" alt="Bot Demo">
</details>

## Comandos para Usar el Bot

<b><details><summary>Toca aquí para ver los Comandos del Bot</summary>

🖍️ Comandos del Bot Principal:

- `/start` : Con este comando puedes verificar si el bot está activo.
- `/link` : Responde a un archivo multimedia para obtener un enlace compartible.
- `/batch` : Genera enlaces compartibles para múltiples archivos a la vez. Úsalo así: `/batch (enlace_primera_publicación) (enlace_última_publicación)`. Asegúrate de que el bot sea administrador en tu canal de almacenamiento.
- `/base_site` : Establece tu dominio de acortador de URL. Uso: `/base_site tudominio.com`.
- `/api` : Establece tu clave API del acortador de URL. Uso: `/api (tu_clave_api)`.
- `/addpremium [ID]` : Otorga acceso premium a un usuario (solo administradores).
- `/addpremium [ID] [días]` : Otorga acceso premium por `X` días a un usuario (solo administradores).
- `/delpremium [ID]` : Revoca el acceso premium de un usuario (solo administradores).
- `/stats` : Muestra estadísticas de usuarios (solo administradores).
- `/deletecloned` : Elimina tu bot clonado. Uso: `/deletecloned (tu_token_de_bot)`.
- `/broadcast` : Responde a un mensaje para enviarlo a todos los usuarios del bot (solo propietario/administradores).
- `/dbroadcast` : Responde a un mensaje para enviarlo a todos los usuarios del bot, y se auto-borrará después de un tiempo (solo propietarios/administradores).

🖍️ Comandos del Bot Clon:

- `/start` : Con este comando puedes verificar si el bot está activo.
- `/link` : Responde a un archivo multimedia para obtener un enlace compartible.
- `/base_site` : Establece tu dominio de acortador de URL. Uso: `/base_site tudominio.com`.
- `/api` : Establece tu clave API del acortador de URL. Uso: `/api (tu_clave_api)`.
- `/broadcast` : Responde a un mensaje para enviarlo a todos los usuarios del bot clon (solo propietario del bot clon).

</b>
</details>

## Créditos

<b><details><summary>Toca aquí para ver los Créditos</summary>

💝 Crédito a [Tech VJ](https://telegram.me/Kingvj01)

🖍️ Este Código Está Totalmente Escrito o Codificado y Publicado por [Tech VJ](https://telegram.me/Kingvj01), ¡Así que no olvides dar Crédito!

💖 ¡Y Muchas Gracias a Todos los que Ayudaron en este Viaje! 💕

Copyright ©️ [Tech VJ](https://telegram.me/Kingvj01)

</b>
</details>

## Sobre el Propietario

<b><details><summary>Toca aquí para ver los Detalles del Propietario</summary>

- Canal de YouTube : [Tech VJ](https://youtube.com/@Tech_VJ)
- Canal de Telegram : [VJ Botz](https://telegram.me/VJ_Botz)
- Enlace de Contacto : [King VJ](https://telegram.me/Kingvj01)
- Enlace de ID de Instagram : [Tech VJ](https://instagram.com/tech.vj)

</b>
</details>


### Copyright ©️ [Tech VJ](https://telegram.me/Kingvj01)

<b>La Venta de este Repositorio o Código de este Repositorio por Dinero Está Estrictamente Prohibida 🚫</b>

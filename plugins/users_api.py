# © Telegram : @KingVJ01 , GitHub : @VJBots

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import requests
import json
from motor.motor_asyncio import AsyncIOMotorClient
from plugins.clone import mongo_db # Asegurarse de que esta importación sea correcta si se usa

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

async def get_short_link(user, link):
    api_key = user["shortener_api"]
    base_site = user["base_site"]
    # print(user) # Quitar este print en producción
    
    # Manejo de casos donde la API o el sitio base no estén configurados
    if not api_key or not base_site:
        # Podrías loggear esto si es un problema, pero para el usuario solo devuelve el link original
        # logging.warning("API Key o Base Site no configurados para el acortador.")
        return link

    try:
        # Asegúrate de usar f"https://{base_site}/api..." ya que tu README.md indica https
        response = requests.get(f"https://{base_site}/api?api={api_key}&url={link}")
        data = response.json()
        
        # Verificar el status_code y el campo "status" en la respuesta JSON
        if response.status_code == 200 and data.get("status") == "success":
            return data.get("shortenedUrl")
        else:
            # Loggear la razón del fallo si es posible
            error_message = data.get("message", "Error desconocido del acortador")
            # logging.error(f"Fallo al acortar URL. Status: {response.status_code}, API response: {error_message}")
            return link # Devolver el enlace original si falla
    except requests.exceptions.RequestException as e:
        # logging.error(f"Error de red o de solicitud al acortador: {e}")
        return link # Devolver el enlace original en caso de error de conexión
    except json.JSONDecodeError as e:
        # logging.error(f"Error al decodificar la respuesta JSON del acortador: {e}")
        return link # Devolver el enlace original si la respuesta no es JSON válido
    except Exception as e:
        # logging.error(f"Error inesperado en get_short_link: {e}")
        return link # Cualquier otro error inesperado


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt in telegram @KingVJ01

async def get_user(user_id):
    user_id = int(user_id)
    # Asume que 'mongo_db.user' es la colección principal de usuarios
    # Si 'mongo_db' es la instancia de MongoClient, entonces sería mongo_db.DB_NAME.users
    # Pero si 'mongo_db' ya es la base de datos, entonces es mongo_db.users
    # Aquí usaré la colección 'users' directamente, asumiendo que 'db' en dbusers.py ya la maneja.
    # Si plugins/users_api.py se usa para manejar la configuración del acortador
    # de forma independiente a la DB principal de usuarios del bot, entonces
    # la lógica de la línea siguiente debe ser consistente.
    
    # Importante: Si 'mongo_db' en este archivo es para bots clonados,
    # y 'db' en plugins/dbusers.py es para la DB principal de usuarios,
    # entonces necesitas una conexión separada para la DB principal de usuarios aquí
    # o reevaluar la estructura. Para este parche, asumiré que esta 'get_user'
    # apunta a la misma colección que plugins/dbusers.py
    
    # Para la DB principal, usa la misma conexión que en plugins/dbusers.py
    # Recomiendo que users_api.py NO tenga su propia conexión a mongo_db,
    # sino que reciba la instancia de la DB de plugins/dbusers.py o una similar.
    # Por ahora, usaré la misma importación de `db` que en plugins/commands.py para consistencia.
    from plugins.dbusers import db as main_db_instance # Importar la instancia global de la DB principal

    user = await main_db_instance.col.find_one({"id": user_id}) # Usar el campo 'id' de la DB principal
    if not user:
        # Si el usuario no existe en la DB principal, no podemos establecer su API.
        # Esto indica un posible problema de flujo, ya que `commands.py` ya debería haber añadido al usuario.
        # Aquí solo vamos a devolver un diccionario vacío o None para indicar que no hay datos.
        # La creación de un nuevo documento con shortener_api/base_site debería ocurrir
        # cuando el usuario es añadido por primera vez al sistema, no solo al intentar obtener su API.
        
        # Para evitar añadir un usuario "dummy" aquí, que podría duplicar lógica con plugins/dbusers.py:
        # Puedes simplemente devolver None y manejarlo en la función que llama.
        # O, si plugins/users_api.py se encarga EXCLUSIVAMENTE de la configuración del acortador,
        # entonces su propia colección `col` debería ser usada para añadir estos datos si no existen.
        
        # Asumiendo que esta `get_user` SÓLO maneja la configuración del acortador y la guarda en una colección separada
        # Si la colección `col` aquí es para la configuración del acortador, la definimos.
        # Si `mongo_db` es la colección de bots clonados (como en plugins/clone.py), esta no es la colección correcta.
        
        # **Opción recomendada: users_api.py no debería tener su propia lógica de DB.
        # Debería recibir los datos del usuario de plugins/commands.py (que los obtiene de plugins/dbusers.py).**
        # No obstante, si se desea una colección separada para acortadores:
        # (Esto requeriría configurar `CDB_NAME` y `CLONE_DB_URI` para esto,
        # o crear una nueva variable de entorno y conexión para la DB de acortadores)
        
        # Para el propósito de este parche y sin cambiar `config.py` o añadir otra conexión,
        # haré que `get_user` y `update_user_info` en `plugins/users_api.py` usen la misma `db`
        # que se importa de `plugins/dbusers.py`. Esto significa que los campos `shortener_api`
        # y `base_site` se añadirán a la colección `users` principal.
        
        # Lógica actualizada para usar la DB principal (plugins/dbusers.py.db)
        # Esto asume que main_db_instance.col es `db.users`
        
        res = {
            "id": user_id, # Usar 'id' para consistencia con plugins/dbusers.py
            "shortener_api": None,
            "base_site": None,
        }
        await main_db_instance.col.update_one( # Usar update_one con upsert=True
            {"id": user_id},
            {"$setOnInsert": res}, # Insertar si no existe
            upsert=True
        )
        user = await main_db_instance.col.find_one({"id": user_id}) # Buscar de nuevo
    return user


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt in telegram @KingVJ01

async def update_user_info(user_id, value:dict):
    user_id = int(user_id)
    from plugins.dbusers import db as main_db_instance # Importar la instancia global de la DB principal
    
    myquery = {"id": user_id} # Usar 'id' para consistencia
    newvalues = { "$set": value }
    await main_db_instance.col.update_one(myquery, newvalues)


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt in telegram @KingVJ01

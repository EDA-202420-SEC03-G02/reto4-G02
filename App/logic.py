import time
import csv
from datetime import datetime
from DataStructures import graph as g
from DataStructures import map_linear_probing as mp
from DataStructures import queue 
from DataStructures import array_list as lt
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        'social_graph': g.new_graph()  
    }
    return catalog
pass

# Funciones para la carga de datos

def load_data(catalog, relationships_file, users_file):
    """
    Carga los datos de relaciones y usuarios en el grafo.
    """
    # Cargar relaciones  #"C:\\Users\\dfeli\\Downloads\\Universidad Segundo Semestre\\Estructura De Datos Y Algoritmos\\Retos\\Reto 4\\reto4-G02\\Data\\relationships_large.csv"
    relationships_file = r"C:\\Users\\danie\\Downloads\\reto 4\\reto4-G02\\Data\\relationships_80.csv"
    #No borrar las direcciones de los demas solo comentarlas
    file1 = csv.DictReader(open(relationships_file, encoding="ISO-8859-1"), delimiter=';')

    for row in file1:
        follower_id = row["FOLLOWER_ID"]
        followed_id = row["FOLLOWED_ID"]
        start_date = datetime.strptime(row["START_DATE"], "%Y-%m-%d %H:%M:%S") if row["START_DATE"] else None
        
        # Agregar la conexión al grafo
        g.add_edge(catalog['social_graph'], follower_id, followed_id)

    # Cargar usuarios  #"C:\\Users\\dfeli\\Downloads\\Universidad Segundo Semestre\\Estructura De Datos Y Algoritmos\\Retos\\Reto 4\\reto4-G02\\Data\\users_info_large.csv"
    users_file = r"C:\\Users\\danie\\Downloads\\reto 4\\reto4-G02\\Data\\users_info_80.csv"
    #No borrar las direcciones de los demas solo comentarlas 
    file2 = csv.DictReader(open(users_file, encoding="ISO-8859-1"), delimiter=';')
    for row in file2:
        user_id = row["USER_ID"]
        user_name = row["USER_NAME"] if row["USER_NAME"] else "Unknown"
        user_type = row["USER_TYPE"] if row["USER_TYPE"] else "Unknown"
        age = int(row["AGE"]) if row["AGE"].isdigit() else None
        join_date = datetime.strptime(row["JOIN_DATE"], "%d/%m/%Y") if row["JOIN_DATE"] else None
        city = row["CITY"] if row["CITY"] else None
        latitude = float(row["LATITUDE"]) if row["LATITUDE"] else None
        longitude = float(row["LONGITUDE"]) if row["LONGITUDE"] else None
        photo = row["PHOTO"] if row["PHOTO"] else None
        hobbies = row["HOBBIES"] if row["HOBBIES"] else None
        
        # Agregar el usuario al grafo
        g.insert_vertex(catalog['social_graph'], user_id, {
            "name": user_name,
            "type": user_type,
            "age": age,
            "join_date": join_date,
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "photo": photo,
            "hobbies": hobbies
        })

    # Reportar estadísticas
    total_users = g.num_vertices(catalog['social_graph'])
    total_connections = g.num_edges(catalog['social_graph'])
    user_types = count_user_types(catalog['social_graph'])
    average_followers_value = average_followers(catalog['social_graph'])
    city_with_most_users_value = city_with_most_users(catalog['social_graph'])

    return total_users, total_connections, user_types, average_followers_value, city_with_most_users_value

def count_user_types(graph):
    """
    Cuenta el número de usuarios según su tipo (basic o premium).
    """
    user_types = {'basic': 0, 'premium': 0}
    for user in mp.get_keys(graph["information"]):
        user_info = mp.get(graph["information"], user)
        if user_info:
            user_type = user_info.get('type')
            if user_type in user_types:
                user_types[user_type] += 1
    return user_types

def get_followers(graph, user_id):
    """
    Retorna una lista de seguidores para un usuario dado.
    """
    followers = []
    for edge in graph['edges']:
        if edge[1] == user_id:
            followers.append(edge[0])  
    return followers

def average_followers(graph):
    """
    Calcula el promedio de seguidores por usuario en el grafo.
    """
    total_followers = 0
    total_users = g.num_vertices(graph)
    
    for user_id in mp.get_keys(graph["vertices"]):
        total_followers += len(get_followers(graph, user_id))  
        
    return total_followers / total_users if total_users > 0 else 0

def city_with_most_users(graph):
    """
    Determina la ciudad con más usuarios en el grafo.
    """
    city_count = {}
    
    for user_id in mp.get_keys(graph["information"]):
        user_info = mp.get(graph["information"], user_id)
        if user_info and 'city' in user_info:
            city = user_info['city']
            if city in city_count:
                city_count[city] += 1
            else:
                city_count[city] = 1

    if city_count:
        most_users_city = max(city_count, key=city_count.get)
        return most_users_city, city_count[most_users_city]
    
    return None, 0

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    user_info = mp.get(catalog['social_graph']["information"], id)
    return user_info
pass


def is_visited(visited_list, user_id):
    """
    Verifica si un usuario ha sido visitado.

    Args:
        visited_list (list): Lista de usuarios visitados.
        user_id (str): ID del usuario a verificar.

    Returns:
        bool: True si el usuario ha sido visitado, False en caso contrario.
    """
    return user_id in visited_list

def req_1(catalog, start_id, end_id):
    """
    Retorna el resultado del requerimiento 1: identifica la red de personas entre dos usuarios.
    
    Args:
        catalog (dict): El catálogo que contiene el grafo social.
        start_id (str): ID del usuario de origen.
        end_id (str): ID del usuario de destino.

    Returns:
        dict: Un diccionario con el tiempo de ejecución, cantidad de personas en el camino,
              y detalles del camino.
    """
    start_time = time.time()  # Iniciar el temporizador

    # BFS
    my_queue = queue.new_queue()  # Crear una nueva cola
    queue.enqueue(my_queue, (start_id, [start_id]))  # Encolar el nodo inicial con el camino
    visited = []  # Usamos una lista para rastrear los nodos visitados

    while not queue.is_empty(my_queue):
        current_id, path = queue.dequeue(my_queue)  # Obtener el nodo actual y el camino hasta él

        # Verificar si el nodo actual es el destino
        if current_id == end_id:
            # Obtener detalles de los usuarios en el camino
            user_details = []
            for user_id in path:
                user_info = mp.get(catalog["social_graph"]["information"], user_id)
                if user_info:
                    user_details.append({
                        "id": user_id,
                        "alias": user_info.get("name", "Unknown"),
                        "type": user_info.get("type", "Unknown")
                    })
            execution_time = time.time() - start_time  # Calcular tiempo de ejecución
            return {
                "execution_time": execution_time * 1000,  # Convertir a milisegundos
                "path_length": len(path),
                "path_details": user_details
            }

        # Verificar si el nodo actual ya ha sido visitado
        if current_id not in visited:
            visited.append(current_id)  # Marcar el nodo como visitado
            # Obtener los vecinos del nodo actual
            neighbors = mp.get(catalog['social_graph']["vertices"], current_id)
            if neighbors:  # Verificar que hay vecinos
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.enqueue(my_queue, (neighbor, path + [neighbor]))

    # Si no se encuentra un camino
    return {
        "execution_time": time.time() - start_time,
        "path_length": 0,
        "path_details": []
    }




def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, id_a, id_b):
    """
    Retorna los amigos en común entre dos usuarios.

    Args:
        catalog (dict): El catálogo que contiene el grafo social.
        id_a (str): ID del primer usuario.
        id_b (str): ID del segundo usuario.

    Returns:
        dict: Un diccionario con el tiempo de ejecución y los amigos en común.
    """
    start_time = time.time()  # Iniciar el temporizador

    # Obtener los vecinos (amigos) de cada usuario
    friends_a = set(mp.get(catalog['social_graph']['vertices'], id_a) or [])
    friends_b = set(mp.get(catalog['social_graph']['vertices'], id_b) or [])

    # Encontrar amigos en común
    common_friends = friends_a.intersection(friends_b)

    # Construir los detalles de los amigos en común
    common_friends_details = []
    for friend_id in common_friends:
        friend_info = mp.get(catalog['social_graph']['information'], friend_id)
        if friend_info:
            common_friends_details.append({
                "id": friend_id,
                "alias": friend_info.get("name", "Desconocido"),
                "type": friend_info.get("type", "Desconocido")
            })

    execution_time = time.time() - start_time  # Calcular tiempo de ejecución
    return {
        "execution_time": execution_time * 1000,  # Convertir a milisegundos
        "common_friends_count": len(common_friends),
        "common_friends_details": common_friends_details
    }

def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, n):
    """
    Identifica los N usuarios más populares y construye un árbol que conecte a esos usuarios.

    Args:
        catalog (dict): El catálogo que contiene el grafo social.
        n (int): Número de usuarios más populares a consultar.

    Returns:
        dict: Un diccionario con el tiempo de ejecución, detalles de los N usuarios más populares,
              y el árbol que los conecta.
    """
    start_time = time.time()  # Iniciar el temporizador

    # Obtener todos los usuarios y su cantidad de seguidores
    users_followers = []
    for user_id in mp.get_keys(catalog['social_graph']['vertices']):
        followers = get_followers(catalog['social_graph'], user_id)
        user_info = mp.get(catalog['social_graph']['information'], user_id)
        
        # Validar que user_info no sea None
        if user_info is None:
            user_name = "Unknown"
        else:
            user_name = user_info.get('name', 'Unknown')
        
        users_followers.append({
            "id": user_id,
            "name": user_name,
            "followers_count": len(followers)
        })

    # Ordenar por cantidad de seguidores en orden descendente y tomar los N más populares
    users_followers.sort(key=lambda x: x['followers_count'], reverse=True)
    top_users = users_followers[:n]

    # Construir un árbol que conecte a estos N usuarios
    tree = build_tree(catalog['social_graph'], [user['id'] for user in top_users])

    execution_time = time.time() - start_time  # Calcular el tiempo de ejecución

    return {
        "execution_time": execution_time * 1000,  # Convertir a milisegundos
        "top_users": top_users,
        "connection_tree": tree
    }


def build_tree(graph, user_ids):
    """
    Construye un árbol que conecta a los usuarios dados usando BFS.

    Args:
        graph (dict): El grafo social.
        user_ids (list): Lista de IDs de los usuarios a conectar.

    Returns:
        dict: Un árbol de conexiones representado como un diccionario.
    """
    visited = set()
    tree = {}

    # Elegir cualquier usuario como raíz
    root = user_ids[0]
    queue = [(root, None)]  # (nodo actual, nodo padre)

    while queue:
        current, parent = queue.pop(0)
        if current not in visited:
            visited.add(current)
            tree[current] = {
                "parent": parent,
                "children": []
            }
            if parent:
                tree[parent]["children"].append(current)

            # Agregar vecinos que estén en la lista de user_ids
            neighbors = mp.get(graph['vertices'], current)
            for neighbor in neighbors:
                if neighbor in user_ids and neighbor not in visited:
                    queue.append((neighbor, current))

    return tree



def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

import time
import csv
from datetime import datetime
from DataStructures import graph as g
from DataStructures import map_linear_probing as mp
from DataStructures import queue 
from DataStructures import array_list as lt
from DataStructures import index_priority_queue as indx
from DataStructures import priority_queue as priori
from DataStructures import stack as st
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
    start_time = time.time()
    # Cargar relaciones #"C:\\Users\\dfeli\\Downloads\\Universidad Segundo Semestre\\Estructura De Datos Y Algoritmos\\Retos\\Reto 4\\reto4-G02\\Data\\relationships_large.csv"
    relationships_file = r"C:\\Users\\danie\\Downloads\\reto 4\\reto4-G02\\Data\\relationships_large.csv"
    #No borrar las direcciones de los demas solo comentarlas
    file1 = csv.DictReader(open(relationships_file, encoding="ISO-8859-1"), delimiter=';')

    for row in file1:
        follower_id = row["FOLLOWER_ID"]
        followed_id = row["FOLLOWED_ID"]
        start_date = datetime.strptime(row["START_DATE"], "%Y-%m-%d %H:%M:%S") if row["START_DATE"] else None
        
        # Agregar la conexión al grafo
        g.add_edge(catalog['social_graph'], follower_id, followed_id)

    # Cargar usuarios  #"C:\\Users\\dfeli\\Downloads\\Universidad Segundo Semestre\\Estructura De Datos Y Algoritmos\\Retos\\Reto 4\\reto4-G02\\Data\\users_info_large.csv"
    users_file = r"C:\\Users\\danie\\Downloads\\reto 4\\reto4-G02\\Data\\users_info_large.csv"
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
    execution_time=time.time() - start_time
    return total_users, total_connections, user_types, average_followers_value, city_with_most_users_value,execution_time

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
    """
    start_time = time.time()  

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
                "execution_time": execution_time ,  
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




def req_2(catalog, start_id, end_id):
    """
    Retorna el resultado del requerimiento 2,  Identificar la  ruta  con  menos  personas intermedias entre 2 usuarios de la aplicación tipo basic
    """
    # TODO: Modificar el requerimiento 2
    start_time = time.time()  # Iniciar tiempo de ejecución

    # Inicializar la búsqueda
    search = g.new_dijkstra_search(start_id)
    search["visited"][start_id] = 0  # Distancia al origen
    previous = {start_id: None}  # Diccionario para reconstruir el camino

    # Agregar el nodo de inicio a la cola de prioridad
    search["pq"].append((0, start_id))  

    while search["pq"]:
        # Encontrar el nodo con la menor distancia en la cola de prioridad
        current_distance = float('inf')#inicializar valor infinito
        current_id = None
        for distance, node in search["pq"]:
            if distance < current_distance:
                current_distance = distance
                current_id = node

        # Eliminar el nodo con la menor distancia de la cola de prioridad
        search["pq"].remove((current_distance, current_id))

        if current_id == end_id:
            # Hemos llegado al destino, reconstruir el camino
            path = []
            while current_id is not None:
                path.append(current_id)
                current_id = previous.get(current_id, None)
            path.reverse()  # Invertir el camino

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
                "execution_time": execution_time,
                "path_length": len(path) - 1,  # Cantidad de personas intermedias
                "path_details": user_details
            }

        # Marcar el nodo como visitado
        search["visited"][current_id] = current_distance

        # Obtener los vecinos (amigos) del nodo actual
        neighbors = mp.get(catalog['social_graph']["vertices"], current_id)
        if neighbors:
            for neighbor in neighbors:
                user_info = mp.get(catalog["social_graph"]["information"], neighbor)
                if user_info and user_info.get("type") == "basic":  # Solo considerar usuarios "basic"
                    new_distance = current_distance + 1  # La distancia incrementa en 1 por cada salto

                    # Si encontramos una ruta más corta, actualizar distancias y el camino
                    if neighbor not in search["visited"] or new_distance < search["visited"][neighbor]:
                        search["visited"][neighbor] = new_distance
                        previous[neighbor] = current_id
                        search["pq"].append((new_distance, neighbor))  # Agregar a la cola de prioridad

    # Si no se encuentra un camino
    return {
        "execution_time": time.time() - start_time,
        "path_length": 0,
        "path_details": []
    }
pass

def req_3(catalog, user_id):

    """
    Retorna el resultado del requerimiento 3 ,Identificar el amigo de un usuario A con mayor cantidad de seguidores
    """
    # TODO: Modificar el requerimiento 3
    start_time = time.time()  # Iniciar tiempo de ejecución

    # Obtener amigos del usuario A
    friends = mp.get(catalog['social_graph']["vertices"], user_id)
    if not friends:
        return {
            "execution_time": time.time() - start_time,
            "most_popular_friend": None,
            "followers_count": 0
        }

    most_popular_friend = None
    max_followers = -1

    # Iterar sobre los amigos para encontrar el que tiene más seguidores
    for friend_id in friends:
        # Obtener la lista de seguidores del amigo
        followers = get_followers(catalog['social_graph'], friend_id)
        followers_count = len(followers)  # Contar la cantidad de seguidores

        # Verificar si este amigo tiene más seguidores que el actual máximo
        if followers_count > max_followers:
            max_followers = followers_count
            most_popular_friend = friend_id

    execution_time = time.time() - start_time  # Calcular tiempo de ejecución

    return {
        "execution_time": execution_time,
        "most_popular_friend": most_popular_friend,
        "followers_count": max_followers
    }


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


    print("Amigos de id_a:", friends_a)
    print("Amigos de id_b:", friends_b)

    # Encontrar amigos en común
    common_friends = friends_a.intersection(friends_b)
   

    # Construir los detalles de los amigos en común
    common_friends_details = []
    for friend_id in common_friends:
        friend_vertex = g.get_vertex(catalog['social_graph'], friend_id)
        if friend_vertex:
            friend_info = friend_vertex['value']
            
            common_friends_details.append({
                "id": friend_id,
                "alias": friend_info.get("name", "Desconocido"),
                "type": friend_info.get("type", "Desconocido")
            })
        else:
            print(f"El vértice para el ID {friend_id} no se encontró.")

    execution_time = time.time() - start_time  # Calcular tiempo de ejecución


    return {
        "execution_time": execution_time * 1000,  # Convertir a milisegundos
        "common_friends_count": len(common_friends),
        "common_friends_details": common_friends_details
    }

    


def req_5(catalog, id, numero_amigos):
    """
    Retorna el resultado del requerimiento 5.
    
    :param catalog: Catálogo que contiene el grafo social.
    :param id: ID del usuario del que se desean obtener los amigos.
    :param numero_amigos: Número de amigos a retornar.
    :return: Una lista de los amigos filtrados y ordenados.
    """
    # Obtener la lista de amigos del usuario usando la función buscar_amigos
    amigos = lt.new_list()
    for user in mp.get_keys(catalog['social_graph']["information"]):
        # Obtener los seguidores del primer usuario
        followers_of_user1 = get_followers(catalog['social_graph'], user)
        # Obtener los seguidores del segundo usuario
        followers_of_user2 = get_followers(catalog['social_graph'], id)
        if id in followers_of_user1 and user in followers_of_user2:
            lt.add_last(amigos, user)
   
    lista_filtr = lt.new_list()

    for friend_id in amigos["elements"]:
        # Obtener la lista de usuarios seguidos por este amigo
        followed = mp.get(catalog['social_graph']["vertices"], friend_id)
        count_followed = len(followed) if followed else 0
        
        # Obtener información del amigo
        friend_info = mp.get(catalog['social_graph']["information"], friend_id)
        friend_name = friend_info.get("name") if friend_info else "Unknown"
        
        # Obtener seguidores del amigo
        seguidores = get_followers(catalog['social_graph'], friend_id)

        # Crear un diccionario con la información del amigo
        Dict_datos = {
            "id": friend_id,
            "name": friend_name,
            "followed_count": count_followed,
            "seguidores": seguidores
        }
        
        lt.add_last(lista_filtr, Dict_datos)

    # Ordenar usando merge_sort
    def sort_crit(friend_a, friend_b):
        # Ordenar por el número de usuarios seguidos de forma descendente
        return friend_a["followed_count"] > friend_b["followed_count"]
        
    sorted_friends = lt.merge_sort(lista_filtr, sort_crit)
    return sorted_friends["elements"][:numero_amigos]
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


    
def req_7(catalog, user_id, lst_hobbies):
    

    """
    Retorna el resultado del requerimiento 7.
    
    :param catalog: Catálogo que contiene el grafo social.
    :param user_id: ID del usuario de donde partirá la búsqueda.
    :param lst_hobbies: Lista de hobbies de interés para la búsqueda.
    :return: Un diccionario con el tiempo de ejecución, la cantidad de amigos encontrados y la subred.
    """
    start_time = time.time()

    # Convertir hobbies a lista
    hobbies_interes = lst_hobbies.split(",")

    # Inicializar estructuras
    subred = lt.new_list()
    amigos_explicitos = lt.new_list()
    amigos_implicitos = lt.new_list()
    dic_por_id = {}

    # Obtener amigos explícitos según la reciprocidad
    for user in mp.get_keys(catalog['social_graph']["information"]):
        followers_of_user1 = get_followers(catalog['social_graph'], user)
        followers_of_user2 = get_followers(catalog['social_graph'], user_id)
        if user_id in followers_of_user1 and user in followers_of_user2:
            lt.add_last(amigos_explicitos, user)

    # Procesar amigos explícitos
    for amigo_id in amigos_explicitos["elements"]:
        amigo_info = mp.get(catalog['social_graph']["information"], amigo_id)
        if amigo_info:
            hobbies_amigo = amigo_info["hobbies"]
            for hobby in hobbies_amigo:
                if hobby in hobbies_interes:
                    if amigo_id not in dic_por_id:
                        dic_por_id[amigo_id] = {
                            "id": amigo_id,
                            "name": amigo_info["name"],
                            "hobbies": hobbies_amigo,
                            "depth": 1
                        }
                        lt.add_last(subred, dic_por_id[amigo_id])
                    

            # Buscar amigos implícitos (amigos de amigos)
        for amigos in amigos_explicitos:
            for user1 in mp.get_keys(catalog['social_graph']["information"]):
                followers_of_user1 = get_followers(catalog['social_graph'], user1)
                followers_of_user2 = get_followers(catalog['social_graph'], amigos)
                if user_id in followers_of_user1 and user in followers_of_user2:
                    lt.add_last(amigos_implicitos, user1)
            
            
            for amigo_de_amigo_id in amigos_implicitos:
                if amigo_de_amigo_id not in dic_por_id and amigo_de_amigo_id != user_id:
                    amigo_de_amigo_info = mp.get(catalog['social_graph']["information"], amigo_de_amigo_id)
                    if amigo_de_amigo_info:
                        hobbies_amigo_impl = amigo_de_amigo_info["hobbies"].split(",")
                        for hobby in hobbies_amigo_impl:
                            if hobby in hobbies_interes:
                                dic_por_id[amigo_de_amigo_id] = {
                                    "id": amigo_de_amigo_id,
                                    "name": amigo_de_amigo_info["name"],
                                    "hobbies": hobbies_amigo_impl,
                                    "depth": 2
                                }
                                lt.add_last(amigos_implicitos, amigo_de_amigo_id)
                                lt.add_last(subred, dic_por_id[amigo_de_amigo_id])
                                

    # Calcular tiempo de ejecución
    execution_time = time.time() - start_time

    # Retornar resultados
    return {
        "execution_time": execution_time * 1000,  # Milisegundos
        "explicit_friends": len(amigos_explicitos["elements"]),
        "implicit_friends": len(amigos_implicitos["elements"]),
        "subnet": subred
    }
    
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

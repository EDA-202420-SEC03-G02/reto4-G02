from DataStructures import queue
from DataStructures import stack

def new_dfo_search():
    """
    Crea una estructura de busqueda usada en el algoritmo **depth_first_order**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **marked**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pre**: Cola con los vertices visitados en preorden. Se inicializa como una cola vacia.
    - **post**: Cola con los vertices visitados en postorden. Se inicializa como una cola vacia.
    - **reversepost**: Pila con los vertices visitados en postorden inverso. Se inicializa como una pila vacia.

    :returns: Estructura de busqueda
    :rtype: dfo_search
    """
    search = {
        'marked': None,
        'pre': queue.new_queue(),
        'post': queue.new_queue(),
        'reversepost': stack.new_stack()
    }
    return search
def new_dijsktra_search(source):
    """

    Crea una estructura de busqueda usada en el algoritmo **dijsktra**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de origen. Se inicializa en ``source``
    - **visited**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pq**: Cola indexada con los vertices visitados. Se inicializa en ``None``

    :returns: Estructura de busqueda
    :rtype: dijsktra_search
    """
    search = {"source": source, "visited": None, "pq": None}
    return search
def new_dijkstra_search(source):
    """
    Crea una estructura de búsqueda usada en el algoritmo Dijkstra.

    Se crea una estructura de búsqueda con los siguientes atributos:
    - **source**: Vértice de origen. Se inicializa en `source`
    - **visited**: Mapa con los vértices visitados. Se inicializa en un diccionario vacío
    - **pq**: Cola indexada con los vértices visitados. Se inicializa en una lista vacía

    :returns: Estructura de búsqueda
    :rtype: dict
    """
    search = {"source": source, "visited": {}, "pq": []}  # Inicializar visited como un diccionario vacío
    return search
def new_edge(v_a, v_b, weight=0):
    """
    Crea un nuevo arco entrelos vertices ``v_a`` y ``v_b`` con un peso ``weight``

    Se crea un arco con los siguientes atributos:

    - **vertex_a**: Vertice A del arco
    - **vertex_b**: Vertice B del arco
    - **weight**: Peso del arco

    :param v_a: Vertice A del arco
    :type v_a: any
    :param v_b: Vertice B del arco
    :type v_b: any
    :param weight: Peso del arco
    :type weight: double

    :returns: Arco creado
    :rtype: edge
    """
    edge = {"vertex_a": v_a, "vertex_b": v_b, "weight": weight}
    return edge


def weight(edge):
    """
    Retorna el peso del arco ``edge``

    :param edge: Arco del cual se quiere obtener el peso
    :type edge: edge

    :returns: Peso del arco
    :rtype: double
    """
    return edge["weight"]


def either(edge):
    """
    Retorna el vertice A del arco ``edge``

    :param edge: Arco del cual se quiere obtener el vertice A
    :type edge: edge

    :returns: Vertice A del arco
    :rtype: any
    """
    return edge["vertex_a"]


def other(edge, veither):
    """
    Retorna el vertice del arco ``edge`` que no es igual a ``veither``

    :param edge: Arco del cual se quiere obtener el vertice B
    :type edge: edge
    :param veither: Vertice A del arco
    :type veither: any

    :returns: Vertice B del arco
    :rtype: any
    """
    if veither == edge["vertex_a"]:
        return edge["vertex_b"]
    elif veither == edge["vertex_b"]:
        return edge["vertex_a"]


def set_weight(edge, weight):
    """
    Cambia el peso del arco ``edge`` por el valor ``weight``

    :param edge: Arco al cual se le quiere cambiar el peso
    :type edge: edge
    :param weight: Nuevo peso del arco
    :type weight: double
    """
    edge["weight"] = weight


def compare_edges(edge1, edge2):
    """
    Funcion utilizada en lista de edges para comparar dos edges
    Retorna 0 si los arcos son iguales, 1 si edge1 > edge2, -1 edge1 < edge2

    :param edge1: Arco 1
    :type edge1: edge
    :param edge2: Arco 2
    :type edge2: edge

    :returns: 0 si los arcos son iguales, 1 si edge1 > edge2, -1 edge1 < edge2
    :rtype: int
    """
    e1v = either(edge1)
    e2v = either(edge2)

    if e1v == e2v:
        if other(edge1, e1v) == other(edge2, e2v):
            return 0
        elif other(edge1, e1v) > other(edge2, e2v):
            return 1
        else:
            return -1
    elif e1v > e2v:
        return 1
    else:
        return -1
def new_graph_search(source):
    """
    Crea una estructura de busqueda usada en los algoritmos **bfs** y **dfs**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de inicio del recorrido. Se usa el vertice ``source``
    - **visited**: Mapa con los vertices visitados. Se inicializa en ``None``

    :param source: Vertice de inicio del recorrido
    :type source: any

    :returns: Estructura de busqueda
    :rtype: graph_search
    """

    search = {"source": source, "visited": None}

    return search    
def new_prim_search(source):
    """
    Crea una estructura de busqueda usada en el algoritmo **prim**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de inicio del MST.
    - **edge_to**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **dist_to**: Mapa con las distancias a los vertices. Se inicializa en ``None``
    - **marked**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pq**: Cola de prioridad indexada (index_priority_queue). Se inicializa en ``None``
    - **mst**: Cola con los vertices visitados en postorden inverso. Se inicializa en ``None``

    :returns: Estructura de busqueda
    :rtype: prim_search
    """

    search = {
        "source": source,
        "edge_to": None,
        "dist_to": None,
        "marked": None,
        "pq": None,
        "mst": None,
    }
    return search
from DataStructures import array_list as al
from DataStructures import map_linear_probing as mp

def new_graph(directed=False):
    """
    Crea un grafo vacío con los atributos necesarios para manejar vértices y aristas.
    
    :param directed: Indica si el grafo es dirigido.
    :type directed: bool
    :returns: Un nuevo grafo vacío.
    :rtype: dict
    """
    graph = {
        "vertices": mp.new_map(150000,0.5),  # Mapa para almacenar los vértices
        "information": mp.new_map(150000,0.5),  # Mapa para almacenar la información de los vértices
        "in_degree": mp.new_map(150000,0.5) if directed else None,  # Mapa para almacenar el grado de entrada (solo si es dirigido)
        "edges":[],  # Contador de aristas
        "directed": directed  # Indica si el grafo es dirigido
    }
    return graph

def insert_vertex(graph, key_vertex, info_vertex=None):
    """
    Inserta un vértice al grafo. Si ya existe, actualiza la información asociada.
    
    :param graph: El grafo donde se insertará el vértice.
    :type graph: dict
    :param key_vertex: La clave del vértice a insertar.
    :type key_vertex: any
    :param info_vertex: Información asociada al vértice (opcional).
    :type info_vertex: any
    """
    if not mp.contains(graph["vertices"], key_vertex):
        mp.put(graph["vertices"], key_vertex, al.new_list())  # Lista vacía de adyacencia
        mp.put(graph["information"], key_vertex, info_vertex)
        if graph["directed"] and graph["in_degree"] is not None:
            mp.put(graph["in_degree"], key_vertex, 0)  # Inicializa grado de entrada
    else:
        mp.put(graph["information"], key_vertex, info_vertex)  # Actualiza información

def add_edge(graph, vertex_a, vertex_b):
    """
    Agrega una arista entre dos vértices en el grafo.
    
    :param graph: El grafo en el que se agregará la arista.
    :param vertex_a: El ID del primer vértice.
    :param vertex_b: El ID del segundo vértice.
    """
    # Asegurarse de que ambos vértices existan en el grafo
    if not mp.contains(graph['vertices'], vertex_a):
        mp.put(graph['vertices'], vertex_a, [])
    if not mp.contains(graph['vertices'], vertex_b):
        mp.put(graph['vertices'], vertex_b, [])

    # Agregar la arista a la lista de aristas
    graph['edges'].append((vertex_a, vertex_b))
    
    # Agregar el vértice B a la lista de vecinos de A
    neighbors_a = mp.get(graph['vertices'], vertex_a)
    if vertex_b not in neighbors_a:
        neighbors_a.append(vertex_b)
        mp.put(graph['vertices'], vertex_a, neighbors_a)
    
    # Si el grafo es dirigido, no se agrega la arista en sentido inverso
    if graph['directed']:
        return

    # Si el grafo no es dirigido, agregar el vértice A a la lista de vecinos de B
    neighbors_b = mp.get(graph['vertices'], vertex_b)
    if vertex_a not in neighbors_b:
        neighbors_b.append(vertex_a)
        mp.put(graph['vertices'], vertex_b, neighbors_b)

def num_vertices(graph):
    """Retorna el número de vértices en el grafo."""
    return mp.size(graph["vertices"])

def num_edges(graph):
    """Retorna el número de arcos en el grafo."""
    return len(graph["edges"])

def vertices(graph):
    """Retorna una lista con todos los vértices del grafo."""
    return mp.get_keys(graph["vertices"])  # Obtener todas las llaves de la tabla hash

def edges(graph):
    """
    Retorna una lista con todos los arcos del grafo.
    
    :param graph: Grafo del que se obtienen los arcos.
    :type graph: dict
    :return: Lista de arcos en el grafo.
    :rtype: list
    """
    edge_list = al.new_list()
    visited = set()  # Para evitar duplicados en grafos no dirigidos

    for vertex in vertices(graph):
        adj_list = mp.get(graph["vertices"], vertex)
        for edge in adj_list:
            vertex_b = edge["vertex_b"]
            if graph["directed"] or (vertex, vertex_b) not in visited:
                al.add_last(edge_list, edge)
                if not graph["directed"]:
                    visited.add((vertex_b, vertex))

    return edge_list

def degree(graph, key_vertex):
    """
    Retorna el número de arcos asociados al vértice con llave `key_vertex`.
    Retorna None si el vértice no existe.
    
    :param graph: El grafo que contiene el vértice.
    :type graph: dict
    :param key_vertex: La clave del vértice.
    :type key_vertex: any
    :return: Número de arcos asociados al vértice o None.
    :rtype: int or None
    """
    if not mp.contains(graph["vertices"], key_vertex):
        return None
    adj_list = mp.get(graph["vertices"], key_vertex)
    return al.size(adj_list)

def in_degree(graph, key_vertex):
    """
    Retorna el número de arcos que llegan al vértice con llave `key_vertex`.
    Retorna None si el vértice no existe.
    
    :param graph: El grafo que contiene el vértice.
    :type graph: dict
    :param key_vertex: La clave del vértice.
    :type key_vertex: any
    :return: Número de arcos que llegan al vértice o None.
    :rtype: int or None
    """
    if not graph["directed"] or not mp.contains(graph["vertices"], key_vertex):
        return None

    return mp.get(graph["in_degree"], key_vertex) if graph["in_degree"] else None
import sys
import App.logic as lg
from tabulate import tabulate
from datetime import datetime

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return lg.new_logic()
pass

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    
    total_users, total_connections, user_types, average_followers, city_with_most_users,time = lg.load_data(control, "relationships_large.csv", "users_info_large.csv")

    print(f"\nTotal de usuarios cargados: {total_users}")
    print(f"Total de conexiones cargadas: {total_connections}")
    print("Tiempo de ejecución:", f"{time:.3f}", "[ms]")
    
    print("\nTipos de usuarios:")
    display_user_types(user_types)
    
    print(f"\nPromedio de seguidores por usuario: {average_followers:.2f}")
    print(f"\nCiudad con más usuarios: {city_with_most_users[0]} con {city_with_most_users[1]} usuarios.")

def display_user_types(user_types):
    """
    Muestra la información de los tipos de usuarios en formato tabular.
    """
    table = []
    for user_type, count in user_types.items():
        table.append([user_type, count])

    print(tabulate(table, headers=["Tipo de Usuario", "Cantidad"], tablefmt="fancy_grid"))



def print_data(control, id):
    """
    Función que imprime un dato dado su ID.

    Args:
        control (dict): Control con la referencia al catálogo.
        id (str): ID del usuario a buscar.
    """
    user_info = lg.get_data(control['catalog'], id)

    if user_info:
        print("Información del usuario:")
        print(f"ID: {id}")
        print(f"Alias: {user_info.get('name', 'Desconocido')}")
        print(f"Tipo: {user_info.get('type', 'Desconocido')}")
    else:
        print(f"No se encontró información para el usuario con ID: {id}")
def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola.
    """
    # Solicitar el ID del usuario de origen
    start_id = input("Ingrese el ID del usuario de origen: ")
    # Solicitar el ID del usuario de destino
    end_id = input("Ingrese el ID del usuario de destino: ")

    # Llamar a la función que obtiene el camino entre los usuarios
    resultados = lg.req_1(control, start_id, end_id)

    # Imprimir el tiempo de ejecución
    print("Tiempo de ejecución:", f"{resultados['execution_time'] :.3f}", "[ms]")  

    # Imprimir el total de personas en el camino
    print(f"Total de personas en el camino: {resultados['path_length']}")

    # Imprimir los detalles del camino
    if resultados['path_length'] > 0:
        print("=" * 80)
        print("Detalles del camino:")
        table_path = []
        for user in resultados['path_details']:
            table_path.append([user['id'], user['alias'], user['type']])
        
        headers_path = ["ID", "Alias", "Tipo"]
        print(tabulate(table_path, headers=headers_path, tablefmt="grid"))
    else:
        print("No se encontró un camino entre los usuarios especificados.")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    # Solicitar el ID del usuario de origen
    start_id = input("Ingrese el ID del usuario de origen: ")
    # Solicitar el ID del usuario de destino
    end_id = input("Ingrese el ID del usuario de destino: ")

    # Llamar a la función que obtiene el camino entre los usuarios
    resultados = lg.req_2(control, start_id, end_id)

    # Imprimir el tiempo de ejecución
    print("Tiempo de ejecución:", f"{resultados['execution_time']:.3f}", "[ms]")

    # Imprimir la cantidad de personas en el camino
    print("Cantidad de personas en el camino:", resultados['path_length'])

    # Imprimir los detalles del camino
    print("Detalles del camino:")
    print(tabulate(
        [[user["id"], user["alias"], user["type"]] for user in resultados['path_details']],
        headers=["ID", "Alias", "Tipo"],
        tablefmt="grid"
    ))
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    # Solicitar el ID del usuario
    user_id = input("Ingrese el ID del usuario: ")

    # Llamar a la función que obtiene el resultado del requerimiento 3
    resultados = lg.req_3(control, user_id)

    # Imprimir el tiempo de ejecución
    print("Tiempo de ejecución:", f"{resultados['execution_time']:.3f}", "[ms]")

    # Imprimir el amigo más popular
    if resultados['most_popular_friend'] is not None:
        print("Amigo más popular:", resultados['most_popular_friend'])
        print("Cantidad de seguidores:", resultados['followers_count'])
    else:
        print("El usuario no tiene amigos.")
    pass


def print_req_4(control):
    """
    Función que imprime la solución del Requerimiento 4 en consola.
    """
    # Solicitar los IDs de los usuarios
    id_a = input("Ingrese el ID del primer usuario: ")
    id_b = input("Ingrese el ID del segundo usuario: ")

    # Llamar a la función que obtiene los amigos en común
    resultados = lg.req_4(control, id_a, id_b)

    # Imprimir el tiempo de ejecución
    print("Tiempo de ejecución:", f"{resultados['execution_time'] :.3f}", "[ms]")

    # Imprimir el total de amigos en común
    print(f"Total de amigos en común: {resultados['common_friends_count']}")

    # Imprimir los detalles de los amigos en común
    if resultados['common_friends_count'] > 0:
        print("=" * 80)
        print("Detalles de los amigos en común:")
        table_friends = []
        for friend in resultados['common_friends_details']:
            table_friends.append([friend['id'], friend['alias'], friend['type']])

        headers_friends = ["ID", "Alias", "Tipo"]
    
        print(tabulate(table_friends, headers=headers_friends, tablefmt="grid"))
    else:
        print("No se encontraron amigos en común entre los usuarios especificados.")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
    Función que imprime la solución del Requerimiento 6 en consola.
    """
    # Solicitar el número de usuarios más populares
    n = int(input("Ingrese el número de usuarios más populares a consultar: "))

    # Llamar a la función que obtiene los N usuarios más populares y su árbol de conexión
    resultados = lg.req_6(control, n)

    # Imprimir el tiempo de ejecución
    print("Tiempo de ejecución:", f"{resultados['execution_time']:.3f}", "[ms]")

    # Imprimir los N usuarios más populares
    print(f"Los {n} usuarios más populares:")
    table_users = []
    for user in resultados['top_users']:
        table_users.append([user['id'], user['name'], user['followers_count']])

    headers_users = ["ID", "Nombre", "Seguidores"]
    print(tabulate(table_users, headers=headers_users, tablefmt="grid"))

    # Imprimir el árbol de conexión
    print("=" * 80)
    print("Árbol de conexión entre los usuarios más populares:")
    for node, info in resultados['connection_tree'].items():
        print(f"Usuario {node}:")
        print(f"  Padre: {info['parent']}")
        print(f"  Hijos: {', '.join(info['children']) if info['children'] else 'Ninguno'}")




def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

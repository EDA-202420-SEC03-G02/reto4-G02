import sys
import App.logic as lg
from tabulate import tabulate
from datetime import datetime
from DataStructures import array_list as lt


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
    
    total_users, total_connections, user_types, average_followers, city_with_most_users = lg.load_data(control, "relationships_large.csv", "users_info_large.csv")

    print(f"\nTotal de usuarios cargados: {total_users}")
    print(f"Total de conexiones cargadas: {total_connections}")
    
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
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

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
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola.
    """
    # Solicitar el ID del usuario
    user_id = input("Ingrese el ID del usuario: ")
    # Solicitar el número de amigos a retornar
    numero_amigos = int(input("Ingrese el número de amigos a retornar: "))

    # Llamar a la función que obtiene los amigos del usuario
    resultados = lg.req_5(control, user_id, numero_amigos)

    # Imprimir el total de amigos encontrados
    print(f"Total de amigos encontrados: {len(resultados)}")

    # Imprimir los detalles de los amigos
    if resultados:
        print("=" * 80)
        print("Detalles de los amigos:")
        table_friends = []
        for friend in resultados:
            table_friends.append([friend['id'], friend['name'], friend['followed_count'], len(friend['seguidores'])])
        
        headers_friends = ["ID", "Nombre", "Número de Seguidos", "Número de Seguidores"]
        print(tabulate(table_friends, headers=headers_friends, tablefmt="grid"))
    else:
        print("No se encontraron amigos para el usuario especificado.")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
    Función que imprime la solución del Requerimiento 7 en consola.
    """
    # Solicitar el ID del usuario de origen
    user_id = input("Ingrese el ID del usuario de origen: ")
    # Solicitar la lista de hobbies de interés
    lst_hobbies = input("Ingrese la lista de hobbies de interés (separados por coma): ")

    # Llamar a la función que obtiene la subred de usuarios con intereses similares
    resultados = lg.req_7(control, user_id, lst_hobbies)

    # Imprimir el tiempo de ejecución
    print("Tiempo de ejecución:", f"{resultados['execution_time']:.3f}", "[ms]")  

    # Imprimir la cantidad de amigos explícitos e implícitos encontrados
    print(f"Cantidad de amigos explícitos encontrados: {resultados['explicit_friends']}")
    print(f"Cantidad de amigos implícitos encontrados: {resultados['implicit_friends']}")

    # Imprimir los detalles de la subred
    print("=" * 80)
    print("Detalles de la subred:")

    # Verificar si 'subnet' contiene elementos
    if resultados['subnet']['size'] == 0:
        print("No se encontró una subred de usuarios con intereses similares.")
    else:
        table_subred = []

        # Acceder a los elementos de la subred
        for user in resultados['subnet']['elements']:
            # Verificar que user sea un diccionario con las claves esperadas
            if isinstance(user, dict) and 'id' in user and 'name' in user and 'depth' in user and 'hobbies' in user:
                hobbies = user['hobbies'] if isinstance(user['hobbies'], list) else [user['hobbies']]
                table_subred.append([
                    user['id'],
                    user['name'],
                    user['depth'],
                    ', '.join(hobbies)
                ])
            else:
                print(f"Advertencia: se encontró un elemento no válido en la subred: {user}")

        # Imprimir tabla con los detalles de la subred
        headers_subred = ["ID", "Nombre", "Nivel", "Hobbies"]
        print(tabulate(table_subred, headers=headers_subred, tablefmt="grid"))
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

# Autenticacion.py
#initial screen


from verificacion import create_users_table, validate_credentials

create_users_table()  # Asegúrate de que la tabla exista

def initial_screen():
    print("Pantalla de Inicio\n")
    print("Seleccione una opción:")
    print("1. Tengo una cuenta")
    print("2. Crear cuenta")
    
    opcion = input("\nIngrese el número de opción: ")
    
    return opcion

def enter_credentials():
    print("\nIngrese nombre de usuario y contraseña:")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    return username, password



def create_acc():
    print("\n2. Crear cuenta")
    name = input("Ingrese su nombre completo: ")
    age = input("Ingrese su edad: ")
    username = input("Nombre de usuario: ")
    password = input("Crear contraseña: ")
    email = input("Correo electrónico: ")



    # Validar si el usuario ya existe
    if validate_credentials(username, password):
        print("Error: El usuario ya existe.")
        return None

    return name, age, username, password, email


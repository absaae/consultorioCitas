# Main.py

from autenticacion import initial_screen, enter_credentials, create_acc
from verificacion import validate_credentials, get_email_from_username, update_password
from pantallaPrincipal import home_screen

def login():
    while True:
        opcion = initial_screen()
        
        if opcion == '1':
            username, password = enter_credentials()
            if validate_credentials(username, password):
                home_screen()
                break
            else:
                print("Error: Credenciales incorrectas.")
                sub_opcion = input("Seleccione una opción:\n1. Volver a pantalla de inicio\n2. Reestablecer contraseña\nIngrese el número de opción: ")
                if sub_opcion == '1':
                    continue
                elif sub_opcion == '2':
                    # Lógica para reestablecer contraseña
                    username = input("\nIngrese nombre de usuario: ")
                    # Verificar si el usuario existe en la base de datos
                    correo = get_email_from_username(username)
                    if correo:
                        # El usuario existe, solicitar nueva contraseña
                        new_password = input("\nIngrese su nueva contraseña: ")
                        update_password(username, new_password)
                        print("\nContraseña actualizada exitosamente.")
                    else:
                        print("\nError: El usuario no existe.")
                    continue
                else:
                    print("\nOpción no válida. Volviendo a pantalla de inicio.")
                    continue
        elif opcion == '2':
            # Crear cuenta y almacenar en la base de datos
            name, age, username, password, email = create_acc()
            # Lógica para almacenar la nueva cuenta en la base de datos (aún no implementada)
            if name and age and username and password and email:
                print(f"\nCuenta para {username} creada exitosamente. Volviendo a pantalla de inicio.")
        else:
            print("\nOpción no válida. Inténtelo nuevamente.")

if __name__ == "__main__":
    login()
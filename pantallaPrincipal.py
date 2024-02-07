# PantallaPrincipal.py
# home screen

from calendarioBD import create_appointment, change_appointment, delete_appointment, consult_appointments
from historialMBD import read_medical_history  

def home_screen():
    print("\nPantalla Principal")
    print("\nOpciones:")
    print("1. Citas")
    print("2. Pagos")
    print("3. Historial clínico")
    opcion = input("\nIngrese el número de opción: ")

    if opcion == '1':
        appointments_menu()
    elif opcion == '2':
        menu_payment()
    elif opcion == '3':
        history_clinic_menu()
    else:
        print("Opción no válida. Inténtelo nuevamente.")

def appointments_menu():
    print("\nMenú de Citas")
    print("1. Crear cita")
    print("2. Modificar cita")
    print("3. Eliminar cita")
    print("4. Consultar citas")
    opcion = input("\nIngrese el número de opción: ")

    if opcion == '1':
        create_appointment_menu()
    elif opcion == '2':
        change_appointment_menu()
    elif opcion == '3':
        delete_appointment_menu()
    elif opcion == '4':
        consult_appointments_menu()
    else:
        print("Opción no válida. Volviendo al menú principal.")

def create_appointment_menu():
    try:
        print("\nCrear Cita")

        date = input("Ingrese la fecha (YYYY-MM-DD): ")
        hour = input("Ingrese la hora (HH:MM) en formato de 24hrs: ")
        description = input("Ingrese la descripción de la cita: ")

        # Llamada a la función de la base de datos para crear la cita
        id_appointment = create_appointment(date, hour, description)

        print(f"\nCita creada exitosamente. ID de la cita: {id_appointment}")

        # Menú después de crear una cita
        return_to_main_menu()

    except Exception as e:
        print(f"Error al crear la cita: {e}")

def change_appointment_menu():
    try:
        print("\nModificar Cita")

        id_appointment = input("Ingrese el ID de la cita que desea modificar: ")
        new_date = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
        new_hour = input("Ingrese la nueva hora (HH:MM): ")

        # Llamada a la función de la base de datos para modificar la cita
        change_appointment(int(id_appointment), new_date, new_hour)

        print("\nCita modificada exitosamente.")

        # Menú después de modificar una cita
        return_to_main_menu()

    except Exception as e:
        print(f"Error al modificar la cita: {e}")

def delete_appointment_menu():
    try:
        print("\nEliminar Cita")

        id_appointment = input("Ingrese el ID de la cita que desea eliminar: ")

        # Llamada a la función de la base de datos para eliminar la cita
        delete_appointment(int(id_appointment))

        print("\nCita eliminada exitosamente.")

        # Menú después de eliminar una cita
        return_to_main_menu()

    except Exception as e:
        print(f"Error al eliminar la cita: {e}")

def consult_appointments_menu():
    try:
        print("\nConsultar Citas")
        citas = consult_appointments()  # Llamada a la función para obtener las citas
        if not citas:
            print("No hay citas disponibles.")
        else:
            print("\nCitas Programadas:")
            for cita in citas:
                print(f"ID: {cita[0]}, Fecha: {cita[1]}, Hora: {cita[2]}, Descripción: {cita[3]}")

        # Menú después de consultar citas
        return_to_main_menu()

    except Exception as e:
        print(f"Error al consultar citas: {e}")

def return_to_main_menu():
    print("\nMenú de Opciones:")
    print("1. Volver al menú principal")
    print("2. Volver al menú de citas")
    print("3. Salir del sistema")
    opcion = input("\nIngrese el número de opción: ")

    if opcion == '1':
        home_screen()
    elif opcion == '2':
        appointments_menu()
    elif opcion == '3':
        print("Saliendo del sistema.")
        exit()
    else:
        print("Opción no válida. Saliendo del sistema.")
        exit()


def history_clinic_menu():
    print("\nMenú de Historial Clínico")
    print("1. Subir historial")
    print("2. Visualizar historial")
    opcion = input("\nIngrese el número de opción: ")

    if opcion == '1':
        upload_medical_history()
    elif opcion == '2':
        view_medical_history()
    else:
        print("\nOpción no válida. Volviendo al menú principal.")



def upload_medical_history():
    try:
        file_path = input("\nIngrese la ruta del archivo de historial médico (historialMedico.txt): ")

        with open(file_path, "r") as file:
            medical_history = file.read()

        print("\nHistorial médico cargado exitosamente:")
        print(medical_history)

    except FileNotFoundError:
        print(f"\nError: El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"\nError al cargar el historial médico: {e}")

    return_to_main_menu()



def view_medical_history():
    medical_history = read_medical_history()  # Llama a la función para leer el historial médico

    if medical_history:
        print("\nHistorial Médico:")
        print(medical_history)
    else:
        print("\nNo se pudo cargar el historial médico.")

    return_to_main_menu()

def menu_payment():
    print("\nMenú de tipos de pago")
    print("1. Pago en efectivo")
    print("2. Pago con aseguradora")

    opcion = input("\nIngrese el número de opción: ")

    if opcion == '1':
        cash_payment()
    elif opcion == '2':
        insurance_payment()
    else:
        print("\nOpción no válida. Volviendo al menú principal.")

def cash_payment():
    total_amount = 500  # Monto total al azar, puedes cambiarlo según tus necesidades
    print(f"\nPago en efectivo - Total a pagar: ${total_amount}")
    # Desglose del pago, si es necesario, se puede implementar aquí
    return_to_main_menu()

def insurance_payment():
    accepted_insurers = ["Dentegra", "Seguros Atlas", "Ammia"]
    insurer = input("\nIngrese el nombre de la aseguradora: ")

    if insurer in accepted_insurers:
        print("\nPago con aseguradora aprobado.")
    else:
        print("\nError: Aseguradora no aceptada. Solo se aceptan: Dentegra, Seguros Atlas, Ammia.")

    return_to_main_menu()



if __name__ == "__main__":
    home_screen()
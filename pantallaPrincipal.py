# PantallaPrincipal.py
# home screen

from calendarioBD import create_appointment, change_appointment, delete_appointment, consult_appointments

class MedicalSystem:
    def __init__(self):
        self.appointments_manager = AppointmentsManager()
        self.payment_manager = PaymentManager()
        self.medical_history_manager = MedicalHistoryManager()

    def run(self):
        self.home_screen()

    def home_screen(self):
        print("\nPantalla Principal")
        print("\nOpciones:")
        print("1. Citas")
        print("2. Pagos")
        print("3. Historial clínico")
        opcion = input("\nIngrese el número de opción: ")

        if opcion == '1':
            self.appointments_manager.appointments_menu()
        elif opcion == '2':
            self.payment_manager.menu_payment()
        elif opcion == '3':
            self.medical_history_manager.history_clinic_menu()
        else:
            print("Opción no válida. Inténtelo nuevamente.")


class AppointmentsManager:
    def __init__(self):
        pass

    def appointments_menu(self):
        print("\nMenú de Citas")
        print("1. Crear cita")
        print("2. Modificar cita")
        print("3. Eliminar cita")
        print("4. Consultar citas")
        opcion = input("\nIngrese el número de opción: ")

        if opcion == '1':
            self.create_appointment_menu()
        elif opcion == '2':
            self.change_appointment_menu()
        elif opcion == '3':
            self.delete_appointment_menu()
        elif opcion == '4':
            self.consult_appointments_menu()
        else:
            print("Opción no válida. Volviendo al menú principal.")

    def create_appointment_menu(self):
        try:
            print("\nCrear Cita")
            date = input("Ingrese la fecha (YYYY-MM-DD): ")
            hour = input("Ingrese la hora (HH:MM) en formato de 24hrs: ")
            description = input("Ingrese la descripción de la cita: ")

            id_appointment = create_appointment(date, hour, description)

            print(f"\nCita creada exitosamente. ID de la cita: {id_appointment}")

            self.return_to_main_menu()

        except Exception as e:
            print(f"Error al crear la cita: {e}")

    def change_appointment_menu(self):
        try:
            print("\nModificar Cita")
            id_appointment = input("Ingrese el ID de la cita que desea modificar: ")
            new_date = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
            new_hour = input("Ingrese la nueva hora (HH:MM): ")

            change_appointment(int(id_appointment), new_date, new_hour)

            print("\nCita modificada exitosamente.")

            self.return_to_main_menu()

        except Exception as e:
            print(f"Error al modificar la cita: {e}")

    def delete_appointment_menu(self):
        try:
            print("\nEliminar Cita")
            id_appointment = input("Ingrese el ID de la cita que desea eliminar: ")

            delete_appointment(int(id_appointment))

            print("\nCita eliminada exitosamente.")

            self.return_to_main_menu()

        except Exception as e:
            print(f"Error al eliminar la cita: {e}")

    def consult_appointments_menu(self):
        try:
            print("\nConsultar Citas")
            citas = consult_appointments()
            if not citas:
                print("No hay citas disponibles.")
            else:
                print("\nCitas Programadas:")
                for cita in citas:
                    print(f"ID: {cita[0]}, Fecha: {cita[1]}, Hora: {cita[2]}, Descripción: {cita[3]}")

            self.return_to_main_menu()

        except Exception as e:
            print(f"Error al consultar citas: {e}")

    def return_to_main_menu(self):
        print("\nMenú de Opciones:")
        print("1. Volver al menú principal")
        print("2. Volver al menú de citas")
        print("3. Salir del sistema")
        opcion = input("\nIngrese el número de opción: ")

        if opcion == '1':
            medical_system.home_screen()
        elif opcion == '2':
            self.appointments_menu()
        elif opcion == '3':
            print("Saliendo del sistema.")
            exit()
        else:
            print("Opción no válida. Saliendo del sistema.")
            exit()


class PaymentManager:
    def __init__(self):
        pass

    def menu_payment(self):
        print("\nMenú de tipos de pago - Funcionalidad no implementada")

class MedicalHistoryManager:
    def __init__(self):
        pass

    def history_clinic_menu(self):
        print("\nMenú de Historial Clínico")
        print("1. Subir historial")
        print("2. Modificar historial")
        print("3. Visualizar historial")
        opcion = input("\nIngrese el número de opción: ")

        if opcion == '1':
            self.upload_medical_history()
        elif opcion == '2':
            self.modify_medical_history()
        elif opcion == '3':
            self.view_medical_history()
        else:
            print("\nOpción no válida. Volviendo al menú principal.")

    def upload_medical_history(self):
        print("\nEl historial se cargó con éxito.")
        self.return_to_main_menu()

    def modify_medical_history(self):
        print("\nEl historial se modificó con éxito.")
        self.return_to_main_menu()

    def view_medical_history(self):
        print("\n*Se despliega el historial*")
        self.return_to_main_menu()

    def return_to_main_menu(self):
        print("\nMenú de Opciones:")
        print("1. Volver al menú principal")
        print("2. Volver al menú de historial clínico")
        print("3. Salir del sistema")
        opcion = input("\nIngrese el número de opción: ")

        if opcion == '1':
            medical_system.home_screen()
        elif opcion == '2':
            self.history_clinic_menu()
        elif opcion == '3':
            print("Saliendo del sistema.")
            exit()
        else:
            print("Opción no válida. Saliendo del sistema.")
            exit()


if __name__ == "__main__":
    medical_system = MedicalSystem()
    medical_system.run()

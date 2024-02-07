# historialMedicoBD.py

def read_medical_history():
    try:
        with open("historialMedico.txt", "r", encoding="utf-8") as file:
            medical_history = file.read()
        return medical_history
    except FileNotFoundError:
        print("El archivo historialMedico.txt no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al leer el historial médico: {e}")
        return None

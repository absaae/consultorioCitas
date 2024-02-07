# CalendarioBD.py

import sqlite3
from datetime import datetime

def crear_tabla_citas():
    conexion = sqlite3.connect("calendario.db")
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            hour TIME NOT NULL,
            description TEXT,
            estate TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()

crear_tabla_citas()

def create_appointment(date, hour, description):
    conexion = sqlite3.connect("calendario.db")
    cursor = conexion.cursor()

    # Utilizar parámetros de fecha y hora por separado
    cursor.execute('''
        INSERT INTO citas (date, hour, description, estate)
        VALUES (?, ?, ?, 'disponible')
    ''', (date, hour, description))

    # Obtener el ID de la última cita insertada
    id_appointment = cursor.lastrowid

    conexion.commit()
    conexion.close()

    return id_appointment


def change_appointment(id_appointment, new_date, new_hour):
    try:
        conexion = sqlite3.connect("calendario.db")
        cursor = conexion.cursor()

        cursor.execute('''
            UPDATE citas
            SET date = ?, hour = ?
            WHERE id = ?
        ''', (new_date, new_hour, id_appointment))

        conexion.commit()
        conexion.close()

        print("Cita modificada exitosamente.")
    except sqlite3.Error as e:
        print("Error al modificar cita:", e)


def delete_appointment(id_appointment):
    try:
        conexion = sqlite3.connect("calendario.db")
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM citas WHERE id = ?', (id_appointment,))

        conexion.commit()

        print("Cita eliminada exitosamente.")
    except sqlite3.Error as e:
        print("Error al eliminar cita:", e)
    finally:
        # Mover estos fuera del bloque except para asegurar que siempre se cierre la conexión
        if conexion:
            conexion.close()



def consult_appointments():
    try:
        conexion = sqlite3.connect("calendario.db")
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM citas WHERE estate = "disponible"')
        citas = cursor.fetchall()

        conexion.close()

        return citas
    except sqlite3.Error as e:
        print("Error al consultar citas:", e)
        return []
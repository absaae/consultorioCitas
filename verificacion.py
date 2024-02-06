# verificacion.py prueba
import sqlite3

def create_users_table():
    # Conexión a la base de datos (creará la base de datos si no existe)
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    # Crear la tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Insertar un usuario predeterminado
    cursor.execute('INSERT INTO usuarios (name, age, username, password, email) VALUES (?, ?, ?, ?, ?)',
                   ('Usuario Predeterminado', '25', 'usuario1', 'contrasena1', 'correo@predeterminado.com'))

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

# Llamamos a la función create_users_table para asegurarnos de que la tabla exista
create_users_table()

def update_user(username, new_name, new_age, new_username, new_password, new_email):
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        # Actualizar todos los campos del usuario en la base de datos
        cursor.execute('''
            UPDATE usuarios
            SET name = ?, age = ?, username = ?, password = ?, email = ?
            WHERE username = ?
        ''', (new_name, new_age, new_username, new_password, new_email, username))

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close() 

        print("Usuario actualizado exitosamente.")
    except sqlite3.Error as e:
        print("Error al actualizar usuario:", e)

def validate_credentials(username, password):
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        # Buscar el usuario en la base de datos
        cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
        usuario = cursor.fetchone()

        # Cerrar la conexión
        conexion.close()

        # Devolver True si se encontró el usuario, False en caso contrario
        return usuario is not None
    except sqlite3.Error as e:
        print("Error al validar credenciales:", e)
        return False

def get_email_from_username(username):
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        # Buscar el correo del usuario en la base de datos
        cursor.execute('SELECT email FROM usuarios WHERE username = ?', (username,))
        email = cursor.fetchone()

        # Cerrar la conexión
        conexion.close()

        # Devolver el correo o None si el usuario no existe
        return email[0] if email else None
    except sqlite3.Error as e:
        print("Error al obtener correo por usuario:", e)
        return None

def update_password(username, new_password):
    try:
        # Conexión a la base de datos
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        # Actualizar la contraseña del usuario en la base de datos
        cursor.execute('UPDATE usuarios SET password = ? WHERE username = ?', (new_password, username))

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()

    except sqlite3.Error as e:
        print("Error al actualizar contraseña:", e)


# Llamamos a la función create_users_table para asegurarnos de que la tabla exista
create_users_table()
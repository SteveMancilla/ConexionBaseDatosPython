import pyodbc 

# Conexión a la base de datos
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=192.168.56.1;'
                      'DATABASE=dbPrueba;'
                      'UID=sa;'
                      'PWD=continental')

# Crear un cursor
cursor = conn.cursor()


DNI = input("Ingrese DNI a insertar: ")
Nombres = input("Ingrese nombres a insertar: ")
Apellidos = input("Ingrese apellidos a insertar: ")
Direccion = input("Ingrese direccion a insertar: ")
Sexo = int(input("Ingrese sexo a insertar: "))

cursor.execute("INSERT INTO estudiante (DNI, Nombres, Apellidos, Direccion, Sexo) VALUES (?,?,?,?,?)", (DNI, Nombres, Apellidos, Direccion, Sexo))
conn.commit()

print("Datos ingresados correctamente")

# Ejecutar una consulta
cursor.execute('SELECT * FROM estudiante')

# Obtener los resultados
for row in cursor:
    print(row)

# Cerrar la conexión
conn.close()

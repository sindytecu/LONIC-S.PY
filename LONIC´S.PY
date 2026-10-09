import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="empresa"
)

def datos():
    name = input("INGRESE EL NOMBRE DEL EMPLEADO: ")
    entrada = input("INGRESE LA FECHA DE ENTREDA DEL EMPLADO: ")
    salida = int(input("INGRESE LA HORA DE SALIDA DEL EMPLADO"))
    ausencias = int(input("INGRESE CUANTAS AUSENCIAS TIENE EL EMPLEADO: "))
    faltas =int(input("INGRESE CUANTAS FALTAS TIENE EL EMPLEADO: "))

    if conexion.is_connected():
        cursor = conexion.cursor()
        query = "INSERT INTO empleado(Nombre,Entrada,Salida,Ausencias,Faltas) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute (query, (name,entrada,salida,ausencias,faltas))
        conexion.commit()
        print("REGISTRO LISTO")


def read():
    id = int(input("INGRESE EL ID: "))
    if conexion.is_connected():
        cursor = conexion.cursor()
        query = "SELECT * FROM empleado WHERE idempleado=%s"
        cursor.execute(query,(id,))
        dato = cursor.fetchall()
        if dato :
            print("REGISTRO ENCONTRADO")
            print(dato)
        else:
            print("no se emcontro nada")


        
def Update():
    id_actualizar = int(input("INGRESE EL ID PARA ACTUALIZAR: "))
    name = input("INGRESE EL NOMBRE DEL EMPLEADO: ")
    entrada = input("INGRESE LA FECHA DE ENTREDA DEL EMPLADO: ")
    salida = int(input("INGRESE LA HORA DE SALIDA DEL EMPLADO"))
    ausencias = int(input("INGRESE CUANTAS AUSENCIAS TIENE EL EMPLEADO: "))
    faltas =int(input("INGRESE CUANTAS FALTAS TIENE EL EMPLEADO: "))

    if conexion.is_connected():

        cursor = conexion.cursor()
        query = "UPDATE empleado SET Nombre=%s,Entrada=%s,Salida=%s,Ausencias=%s,Faltas=%s WHERE idempleado=%s"
        cursor.execute(query, (name,entrada,salida,ausencias,faltas,id_actualizar))
        conexion.commit()
        print("ACTUALIZACION LISTA")


def delete():
    id_eliminar = int(input("ingrese el id para borrar: "))
    if conexion.is_connected():
        cursor = conexion.cursor()
        query = "DELETE FROM empleado WHERE idempleado=%s"
        cursor.execute(query,(id_eliminar,))
        conexion.commit()
        print("ELIMINADOS!!")


def menu():
    while True:
        print("1.INGRESE LOS DATOS")
        print("2.VER LA TABLA DE DATOS DE LOS EMPLEADOS")
        print("3.ACTUALIZACION")
        print("4.ELIMINAR ALGO DE LA TABLA")

        try:
            desi = int(input("INGRESE QUE OPCION REQUIERE: "))
            if desi ==1:
                datos()
            elif desi ==2:
                read()
            elif desi ==3:
                Update()
            elif desi ==4:
                delete()
                break
            else:
                print("INTENTE DE NUEVO")
        except ValueError:
            print("SOLO NUMEROS, INTENTE DE NUEVO!!")
menu()
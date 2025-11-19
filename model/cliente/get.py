def get(connection):
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM cliente;")

    clientes = cursor.fetchall()
    cursor.close()

    return clientes
def get(connection):
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM servico;")

    servicos = cursor.fetchall()
    cursor.close()

    return servicos
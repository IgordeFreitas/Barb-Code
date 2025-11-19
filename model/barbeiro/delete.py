def delete(connection, id):
    cursor = connection.cursor()
    dados = (id,)
    query = "DELETE FROM barbeiro WHERE id_barbeiro = %s"
    cursor.execute(query, dados)
    cursor.close()
    return cursor.rowcount


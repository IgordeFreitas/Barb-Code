def delete(connection, id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM servico WHERE id_servico = %s", (id,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
def delete(connection, id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM barbeiro_servico WHERE id_barbeiro_servico = %s", (id,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
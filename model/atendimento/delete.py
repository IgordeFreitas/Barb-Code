def delete(connection, id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM atendimento WHERE id_atendimento = %s", (id,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
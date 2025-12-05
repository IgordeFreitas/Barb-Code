def delete(connection, id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM barbeiro WHERE id_barbeiro = %s", (id,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
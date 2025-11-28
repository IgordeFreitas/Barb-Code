def delete(connection, id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM agenda WHERE id_agenda = %s", (id,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
def delete(connection, id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
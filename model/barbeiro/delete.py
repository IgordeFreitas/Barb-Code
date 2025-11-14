def delete(connection):
    cursor = connection.cursor
    cursor.execute("DELETE barbeiro WHERE id_barbeiro = {id}")


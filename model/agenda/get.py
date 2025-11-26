def get(connection):
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM agenda;")

    agenda = cursor.fetchall()
    cursor.close()

    return agenda
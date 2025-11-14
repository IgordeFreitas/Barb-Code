def get(connection):
    print(connection)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select id_barbeiro, nome from barbeiro")

    barbeiros = cursor.fetchall()
    cursor.close()
    
    return barbeiros
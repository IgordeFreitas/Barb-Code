def get(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM barbeiro;")

    barbeiros = cursor.fetchall()
    cursor.close()
    
    return barbeiros
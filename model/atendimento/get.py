def get(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM atendimento;")

    atendimento = cursor.fetchall()
    cursor.close()
    
    return atendimento
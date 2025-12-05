def update(connection, id_barbeiro, id_servico):
    cursor = connection.cursor()
    query = " UPDATE barbeiro_servico SET id_servico = %s WHERE id_barbeiro = %s "
    #UPDATE barbeiro_servico SET id_servico = 2 WHERE id_barbeiro = 3;
    cursor.execute(query,(id_servico, id_barbeiro))
    cursor.close()

    return cursor.rowcount

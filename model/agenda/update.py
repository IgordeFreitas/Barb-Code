def update(connection, idAgenda, novaDataHora, novoStatus, novoIdbarbeiro):
    cursor = connection.cursor()
    query = " UPDATE agenda SET data_hora = %s, status = %s, id_barbeiro = %s WHERE id_agenda = %s"
    dados = (novaDataHora, novoStatus, novoIdbarbeiro, idAgenda)
    cursor.execute(query, dados)
    cursor.close()
    return cursor.rowcount
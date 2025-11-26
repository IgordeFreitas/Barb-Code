def update(connection, novoNome, novoPreco, id):
    cursor = connection.cursor()
    query = " UPDATE servico SET nome = %s, preco = %s WHERE id_servico = %s "
    cursor.execute(query,(novoNome, novoPreco, id))
    cursor.close()
    return cursor.rowcount
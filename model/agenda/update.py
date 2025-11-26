def update(connection, novoNome, novoEmail, novoTelefone, novaSenha, id):
    cursor = connection.cursor()
    query = " UPDATE cliente SET nome = %s, email = %s, telefone = %s, senha = %s WHERE id_cliente = %s "
    cursor.execute(query,(novoNome, novoEmail, novoTelefone, novaSenha, id))
    cursor.close()
    return cursor.rowcount
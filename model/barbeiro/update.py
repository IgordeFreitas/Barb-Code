def update(connection, novoNome, novoCpf, novoEmail, novaSenha, novoTelefone, id):
    cursor = connection.cursor()
    query = " UPDATE barbeiro SET nome = %s, cpf = %s, email = %s, senha = %s, telefone = %s WHERE id_barbeiro = %s "
    cursor.execute(query,(novoNome, novoCpf, novoEmail, novaSenha, novoTelefone, id))
    cursor.close()
    return cursor.rowcount
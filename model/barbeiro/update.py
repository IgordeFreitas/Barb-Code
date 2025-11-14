def update(connection):
    cursor = connection.cursor
    cursor.execute("UPDATE barbeiro SET nome = {noveNome}, cpf = {novoCpf}, email = {novoEmail}, senha = {novaSenha}, telefone = {novoTelefone} WHERE id_barbeiro = {id}")
    cursor.close()
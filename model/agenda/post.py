def post(connection, nome, email, senha, telefone):
    cursor = connection.cursor()

    dados = (nome, email, senha, telefone)
    query = "insert into cliente(nome, email, telefone, senha) values(%s,%s,%s,%s)"
    cursor.execute(query, dados)

    cursor.close()
def post(connection, nome, preco):
    cursor = connection.cursor()

    dados = (nome, preco)
    query = "insert into servico(nome, preco) values(%s,%s)"
    cursor.execute(query, dados)

    cursor.close()
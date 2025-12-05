def post(connection, id_barbeiro, id_servico):
    cursor = connection.cursor()

    dados = (id_barbeiro, id_servico)
    query = "insert into barbeiro_servico(id_barbeiro, id_servico) values(%s,%s)"
    cursor.execute(query, dados)

    cursor.close()
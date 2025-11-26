def post(connection, data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico):
    cursor = connection.cursor()

    dados = (data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico)
    query = "insert into atendimento(data_hora_inicio, data_hora_fim, status, id_barbeiro, id_cliente, id_servico) values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, dados)

    cursor.close()
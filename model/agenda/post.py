def post(connection, dataHora, status, idBarbeiro):
    cursor = connection.cursor()

    dados = (dataHora, status, idBarbeiro)
    query = "insert into agenda(data_hora, status, id_barbeiro) values(%s,%s,%s)"
    cursor.execute(query, dados)

    cursor.close()
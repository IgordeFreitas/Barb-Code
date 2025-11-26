def post(connection, dataHora, status):
    cursor = connection.cursor()

    dados = (dataHora, status)
    query = "insert into agenda(data_hora, status) values(%s,%s)"
    cursor.execute(query, dados)

    cursor.close()
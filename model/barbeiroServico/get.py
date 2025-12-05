def get(connection, id):
    cursor = connection.cursor(dictionary=True)
    sql = 'SELECT id_barbeiro, id_servico FROM barbeiro_servico WHERE id_barbeiro_servico = %s'
    dados = (id,)
    cursor.execute(sql, dados)
    barbeiroServico = cursor.fetchall()
    cursor.close()
    return barbeiroServico
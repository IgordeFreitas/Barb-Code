def get(connection, id):
    cursor = connection.cursor(dictionary=True)
    sql = 'SELECT id_atendimento, id_servico FROM atendimento_servico WHERE id_atendimento_servico = %s'
    dados = (id,)
    cursor.execute(sql, dados)
    atendimentoServico = cursor.fetchall()
    cursor.close()
    return atendimentoServico
def update(connection, novaDataInicio, novaDataFim, novoStatus, novoIdBarbeiro, novoIdCliente, novoIdServico, id):
    cursor = connection.cursor()
    query = "UPDATE atendimento SET data_hora_inicio = %s, data_hora_fim = %s, status = %s, id_barbeiro = %s, id_cliente = %s, id_servico = %s WHERE id_atendimento = %s "
    cursor.execute(query,(novaDataInicio, novaDataFim, novoStatus, novoIdBarbeiro, novoIdCliente, novoIdServico, id))
    cursor.close()
    return cursor.rowcount
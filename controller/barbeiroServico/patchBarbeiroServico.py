from config.dbConfig import getConnection
from model.atendimento.update import update

def patchAtendimento(novaDataInicio, novaDataFim, novoStatus, novoIdBarbeiro, novoIdCliente, novoIdServico, id):
    connection = None
    try:
        connection = getConnection()
        
        ok = update(connection, novaDataInicio, novaDataFim, novoStatus, novoIdBarbeiro, novoIdCliente, novoIdServico, id)
        connection.commit()
        return ok

    except Exception as e:
        if connection:
            connection.rollback()

        print(f"Erro ao fazer o update de atendimento: {e}")
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()
from config.dbConfig import getConnection
from model.barbeiroServico.update import update

def patchBarbeiroServico(id_barbeiro, id_servico):
    connection = None
    try:
        connection = getConnection()
        connection.start_transaction()
        ok = update(connection, id_barbeiro, id_servico)
        connection.commit()
        return ok

    except Exception as e:
        if connection:
            connection.rollback()

        print(f"Erro ao fazer o update do serviço do barbeiro: {e}")
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close() 
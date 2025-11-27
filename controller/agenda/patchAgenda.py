from config.dbConfig import getConnection
from model.agenda.update import update

def patchAgenda(idAgenda, novaDataHora, novoStatus, novoIdBarbeiro):
    connection = None
    try:
        connection = getConnection()
        
        ok = update(connection, idAgenda, novaDataHora, novoStatus, novoIdBarbeiro)
        connection.commit()
        return ok

    except Exception as e:
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500, "e":e}
    finally:
        if connection:
            connection.close()

from config.dbConfig import getConnection
from model.barbeiro.delete import delete

def deletarBarbeiro():
    connection = None
    try:
        connection = getConnection()
        return delete(connection)

    except Exception as e:
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
    
    finally:
        if connection:
            connection.close()

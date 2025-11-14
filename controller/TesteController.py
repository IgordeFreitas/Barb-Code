from config.dbConfig import getConnection
from model.TesteModel import modelTeste

def consultarBarbeiro():
    connection = None
    try:
        connection = getConnection()
        return modelTeste(connection)

    except Exception as e:
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()

from config.dbConfig import getConnection
from model.servico.get import get

def consultarServico():
    connection = None
    try:
        connection = getConnection()
        ok = get(connection)
        connection.commit()
        return ok
    except Exception as e:
        if connection:
            connection.rollback()

        print(f"Erro ao consultar servico: {e}")
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()

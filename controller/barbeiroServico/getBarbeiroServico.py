from config.dbConfig import getConnection
from model.barbeiroServico.get import get

def consultarBarbeiroServico(id):
    connection = None
    try:
        connection = getConnection()
        ok = get(connection, id)
        return ok
    except Exception as e:
        print(f"Erro ao consultar Serviços do barbeiro: {e}")
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()
	

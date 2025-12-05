from config.dbConfig import getConnection
from model.barbeiroServico.get import get

def consultarBarbeiroServicos(id):
    connection = None
    try:
        connection = getConnection()
        ok = get(connection, id)
        return ok
    except Exception as e:
        print("Conexão com o banco falhou")
        print(f"Erro ao consultar Barbeiro Servico: {e}")
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()
	

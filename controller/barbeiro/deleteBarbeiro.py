from config.dbConfig import getConnection
from model.barbeiro.delete import delete

def deletarBarbeiro(id):
    connection = None
    try:
        connection = getConnection()
        ok = delete(connection, id)
        connection.commit()
        return ok
    
    except Exception as e:
        if connection:
            connection.rollback()

        print(f"Erro ao deletar barbeiro: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
    
    finally:
        if connection:
            connection.close()

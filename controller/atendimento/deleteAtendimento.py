from config.dbConfig import getConnection
from model.barbeiro.delete import delete

def deletarBarbeiro(id: int):
    connection = None
    connection = getConnection()
    try:
        rowCount = delete(connection, id)
        connection.commit()
        return rowCount
    except Exception as e:

        connection.rollback() 
        
        print(f"Erro ao deletar barbeiro: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
    finally:
        if connection:
            connection.close()
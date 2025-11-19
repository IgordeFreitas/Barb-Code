from config.dbConfig import getConnection
from model.cliente.get import get

<<<<<<<< HEAD:controller/barbeiro/deleteBarbeiro.py
def deletarBarbeiro(id):
    connection = None
    try:
        connection = getConnection()
        ok = delete(connection, id)
        connection.commit()
        return ok
    
========
def consultarCliente():
    connection = None
    try:
        connection = getConnection()
        return get(connection)

>>>>>>>> 8ffc829 (0.1.5 atualizações no código):controller/cliente/getCliente.py
    except Exception as e:
        if connection:
            connection.rollback()

        print(f"Erro ao deletar barbeiro: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()
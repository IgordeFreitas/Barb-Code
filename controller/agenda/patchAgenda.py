from config.dbConfig import getConnection
from model.cliente.update import update

def patchCliente(novoNome, novoEmail, novoTelefone, novaSenha, id):
    connection = None
    try:
        connection = getConnection()
        
        ok = update(connection, novoNome, novoEmail, novoTelefone, novaSenha, id)
        connection.commit()
        return ok

    except Exception as e:
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500, "e":e}
    finally:
        if connection:
            connection.close()

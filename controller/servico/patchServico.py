from config.dbConfig import getConnection
from model.servico.update import update

def patchServico(novoNome, novoPreco, id):
    connection = None
    try:
        connection = getConnection()
        
        ok = update(connection, novoNome, novoPreco, id)
        connection.commit()
        return ok

    except Exception as e:
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500, "e":e}
    finally:
        if connection:
            connection.close()

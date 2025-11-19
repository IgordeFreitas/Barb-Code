from config.dbConfig import getConnection
from model.barbeiro.update import update

def patchBarbeiro(novoNome, novoCpf, novoEmail, novaSenha, novoTelefone, id):
    connection = None
    try:
        connection = getConnection()
        
        ok = update(connection, novoNome, novoCpf, novoEmail, novaSenha, novoTelefone, id)
        connection.commit()
        return ok

    except Exception as e:
        if connection:
            connection.rollback()

        print(f"Erro ao fazer o update de barbeiro: {e}")
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()

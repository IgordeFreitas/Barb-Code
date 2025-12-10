from config.dbConfig import getConnection
from model.login.post import post

def login(cpf, senha):
    connection = None
    try:
        connection = getConnection()
        login = post(connection, cpf, senha)
        
        if login:
            return {"mensagem": "Login efetuado com sucesso!", "status": 201}
        else:
            return {"mensagem": "Usuário inexistente!", "status": 201}

    except Exception as e:
        print(f"Erro ao efetuar login: {e}") 
        
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()
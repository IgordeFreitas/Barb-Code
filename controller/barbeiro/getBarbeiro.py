from config.dbConfig import getConnection
from model.barbeiro.get import get
from lib.Barbeiro import Barbeiro

def consultarBarbeiro():
    connection = None
    try:
        connection = getConnection()
        ok = get(connection)
        barbeiros = []
        for objeto in ok:
            barbeiro = Barbeiro(objeto['nome'], objeto['email'], objeto['senha'], objeto['telefone'])
            barbeiro.setCpf(objeto['cpf'])
            barbeiro.setId(objeto['id_barbeiro'])
            barbeiros.append(barbeiro)
            
        return barbeiros
    except Exception as e:
        print(f"Erro ao consultar barbeiro: {e}")
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()
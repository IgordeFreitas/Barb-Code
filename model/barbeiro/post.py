    
def post(connection, nome, cpf, email, senha, telefone):
    cursor = connection.cursor()

    dados = (nome, cpf, email, senha, telefone)
    query = "insert into barbeiro(nome, cpf, email, senha, telefone) values(%s,%s,%s,%s,%s)"
    cursor.execute(query, dados)

    cursor.close()

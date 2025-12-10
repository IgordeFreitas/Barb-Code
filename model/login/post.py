def post(connection, cpf, senha):
    print("entrei no cu do lucas")
    cursor = connection.cursor()

    dados = (cpf, senha)
    query = "SELECT * FROM barbeiro WHERE cpf = %s AND senha = %s"
    cursor.execute(query, dados)

    login = cursor.fetchall()
    print("entrei no cu do lucas")
    return login
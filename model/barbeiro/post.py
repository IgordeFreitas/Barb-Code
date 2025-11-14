    
def post(connection):
    cursor = connection.cursor
    cursor.execute("insert into barbeiro(nome, cpf, email, senha, telefone) values('Luccas','111.222.333-52','luccasamcabral@gmail.com','140307','22992383691')")

    barbeiros = cursor.fetchall()
    cursor.close()
    
    return barbeiros
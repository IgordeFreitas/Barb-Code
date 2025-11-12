from config.dbConfig import getConnection

def consultarBarbeiro():
    connection = None
    try:
        connection = getConnection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("select id_barbeiro, nome from barbeiro")

        barbeiros = cursor.fetchall()
        cursor.close()
        
        return {"barbeiros": barbeiros, "status": 200}
        
    except Exception as e:
        return {"erro": "Ao conectar com o banco ou executar a consulta. Veja o console para detalhes.", "status": 500}
        
    finally:
        if connection:
            connection.close()


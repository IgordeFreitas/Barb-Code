from ..controller.TesteController import consultarBarbeiro

sql = "SELECT * FROM barbeiro"

def consultarUsuarios(connectionDB):
    try:
        query = connectionDB.cursor(dictionary=True)
        query.execute(sql)

        usuarios = query.fecthAll()
        query.close

        return usuarios
    
    except mysql.connector.Error as err:
        
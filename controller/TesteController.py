from ..config.dbConfig import getConnection
from ..model.TesteModel import que

def consultarBarbeiro():
    try:
        connection = getConnection()
    finally:
        if connection:
            connection.close()

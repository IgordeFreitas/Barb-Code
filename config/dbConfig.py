import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Verifica se as variáveis foram carregadas
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    print("Erro: As variáveis de ambiente do banco de dados não foram carregadas corretamente. Verifique o arquivo .env.")
    connectionPool = None
else:
    try:
        # Cria o pool de conexões
        connectionPool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name = "pool_barbcode",
            pool_size = 5,
            pool_reset_session = True,
            host = DB_HOST,
            port = DB_PORT,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME
        )
        print('Pool MySQL Criado com Sucesso!')

    except mysql.connector.Error as err:
        print(f"Erro ao criar o pool de conexões: {err}")
        connectionPool = None

# --- Função para obter uma conexão do pool ---
def getConnection():
    if connectionPool is None:
        raise Exception("Erro: o pool de conexões não está disponível. Verifique as configurações do banco de dados.")
    try:
        connection = connectionPool.get_connection()
        return connection
    except mysql.connector.Error as err:
        raise Exception(f"Erro ao obter conexão do pool: {err}")

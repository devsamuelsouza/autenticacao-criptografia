import mysql.connector
from dotenv import dotenv_values
config = dotenv_values(".env")

def Conexao():
        conexao = mysql.connector.connect(
            host=config.get("DATABASE_URL"),
            user=config.get("DATABASE_USER"),
            password=config.get("DATABASE_PASSWORD"),
            database=config.get("DATABASE_NAME"),
            port= int(config.get("DATABASE_PORT", 3306))
        ) 
        if conexao.is_connected():
            return conexao
        else:
            return None
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def Conexao():
        conexao = mysql.connector.connect(
            host=os.getenv("DATABASE_SERVER"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=os.getenv("DATABASE_NAME"),
            port=int(os.getenv("DATABASE_PORT",18356)),
                connection_timeout=30,
        ) 
        if conexao.is_connected():
            return conexao
        else:
            return None
print(Conexao())
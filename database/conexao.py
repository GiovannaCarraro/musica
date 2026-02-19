import mysql.connector

  
def conectar():
        #Conectando no bd
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="Musica"
            )

            #Criando o cursor
        cursor = conexao.cursor(dictionary=True)

        return conexao, cursor
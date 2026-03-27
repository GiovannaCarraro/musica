import mysql.connector

  
def conectar():
        #Conectando no bd
    tipo_conexao = "Nuvem"
    if tipo_conexao == "Local":
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="Musica"
            )

            #Criando o cursor
    else:
        conexao = mysql.connector.connect(
            host="servidor-giovanna-servidor-giovanna.a.aivencloud.com",
            port=28596,
            user="avnadmin",
            password="AVNS_7GpD5nPMfNurZLaW2xD",
            database="Musica")

        cursor = conexao.cursor(dictionary=True)

        return conexao, cursor

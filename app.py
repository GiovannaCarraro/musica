from flask import Flask, render_template
import mysql.connector

app = Flask (__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def pagina_principal():

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

    #Executando a consultando
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    #rec os dados
    musicas =  cursor.fetchall()

    #executando a consulta do genero
    cursor.execute("SELECT nome, icone, cor FROM genero;")

    #rec os dados genero
    generos = cursor.fetchall()

    #fechando a conexao
    conexao.close()


    return render_template("principal.html", musicas = musicas, generos = generos)

if __name__ == "__main__":
    app.run(debug=True)
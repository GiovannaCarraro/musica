from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_musicas
from model.genero import recuperar_generos

app = Flask (__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def pagina_principal():

    #rec musicas

    musicas = recuperar_musicas()
    #rec generos
    generos = recuperar_generos()

    #mostra a pag
    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def pagina_admin():
    #recup as musicas
    musicas = recuperar_musicas()
    #rec os generos
    generos = recuperar_generos()
    #mostra a pag
    return render_template("administracao.html", musicas = musicas, generos = generos)

if __name__ == "__main__":
    app.run(debug=True)
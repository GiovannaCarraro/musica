from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import recuperar_musicas
from model.genero import recuperar_generos
from model.musica import adicionar_musica

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

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("nome_musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    imagem  = request.form.get("imagem")
    genero = request.form.get("genero")
    if  adicionar_musica(nome_musica, cantor, duracao, imagem, genero):
        return redirect("/admin")
    else:
        return "erro ao adicionar musica"
    
if __name__ == "__main__":
    app.run(debug=True)
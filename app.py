from flask import Flask, render_template, request, redirect, session
import mysql.connector
from model.musica import recuperar_musicas
from model.genero import recuperar_generos
from model.musica import adicionar_musica
from model.musica import deletar_musica
from model.musica import ativar_musica
from model.usuario import cadastrar_usuario
from model.usuario import autenticar_usuario

app = Flask (__name__)

app.secret_key = "chiclete"

@app.route("/home", methods=["GET"])
@app.route("/")
def pagina_principal():

    #rec musicas

    musicas = recuperar_musicas(True)
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
    
@app.route("/musica/delete/<codigo>" )
def excluir_musica(codigo):
    deletar_musica(codigo)
    return redirect ("/admin")

@app.route("/musica/ativar/<codigo>/<status>")
def status_musica(codigo, status):
    ativar_musica(codigo, status)
    return redirect ("/admin")

@app.route("/cadastrar")
def pagina_cadastro():
    return render_template("cadastrar.html")

@app.route("/cadastrar", methods= ["POST"])
def logar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if cadastrar_usuario(usuario, senha):
        redirect("/cadastrar")
        session ["usuario"] = "s%"
        return "você acessou"
    else:
        return render_template("cadastrar.html", erro = "Acesso negado!")
    
@app.route("/login", methods=["POST"])
def pagina_login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    login = autenticar_usuario(usuario, senha)

    if login:
        return redirect("/admin")
    else:
        return redirect("/login")
    
    
if __name__ == "__main__":
    app.run(debug=True)
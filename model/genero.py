from database.conexao import conectar
def recuperar_generos():

    conexao, cursor = conectar()

    #executando a consulta do genero
    cursor.execute("SELECT nome, icone, cor FROM genero;")

    #rec os dados genero
    generos = cursor.fetchall()

    #fechando a conexao
    conexao.close()

    return generos
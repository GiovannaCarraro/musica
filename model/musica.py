from database.conexao import conectar

def recuperar_musicas():
    # passo 1 e 2 ja feito
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    #rec os dados
    musicas =  cursor.fetchall()

    # fechar a conexão
    conexao.close()

    return musicas
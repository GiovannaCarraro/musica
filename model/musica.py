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

def adicionar_musica(cantor:str, nome:str, duracao:str, imagem:str, genero:str) -> bool:
    """Está função tem o objetivo de adicionar e salvar musicas no banco de dados"""

    try:
        conexao, cursor = conectar()
        cursor.execute("""
        INSERT INTO MUSICA (CANTOR, NOME, DURACAO, URL_IMAGEM, NOME_GENERO)
        VALUES (%s, %s, %s, %s, %s);
        """, [cantor, nome, duracao, imagem, genero ])
        
        conexao.commit()
        conexao.close()

        return True

    except:
        return False  

def delete():
    conexao, cursor = conectar()  

    cursor.execute("DELETE FROM Musica WHERE ")
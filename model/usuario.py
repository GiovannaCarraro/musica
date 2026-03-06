from database.conexao import conectar

def cadastrar_usuario(usuario:str, senha:str):
    try:
        conexao, cursor = conectar()
    
        cursor.execute("INSERT INTO login (usuario, senha) VALUES (%s, %s)", [usuario, senha])

        conexao.commit()
        conexao.close()
    
        return True

    except:
        return False
    
def autenticar_usuario(usuario:str, senha:str) ->list:
    """Função que verifica se o úsuario está cadastrado, se estiver cadastrado retorna os dedos dele, caso não haja o cadastro, retorna None """

    conexao, cursor = conectar()

    cursor.execute("SELECT usuario, senha FROM LOGIN WHERE usuario = %s and senha = %s", [usuario, senha])
        
    usuario = cursor.fetchone()
    conexao.close()

    return usuario


        

  

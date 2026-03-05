from database.conexao import conectar

def cadastrar_funcionario(usuario:str, senha:str):
    try:
        conexao, cursor = conectar()
    
        cursor.execute("INSERT INTO login (usuario, senha) VALUES (%s, %s)", [usuario, senha])

        conexao.commit()
        conexao.close()
    
        return True

    except:
        return False

  

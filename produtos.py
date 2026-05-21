from banco import conectar

def cadastrar_produto(nome, categoria, preco, quantidade, especificacoes):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome, categoria, preco, quantidade, especificacoes)
    VALUES (?, ?, ?, ?, ?)
    """, (nome, categoria, preco, quantidade, especificacoes))

    conn.commit()
    conn.close()


def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    dados = cursor.fetchall()

    conn.close()
    return dados
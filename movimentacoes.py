from banco import conectar
from datetime import datetime

def entrada_estoque(produto_id, quantidade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade + ?
    WHERE id = ?
    """, (quantidade, produto_id))

    cursor.execute("""
    INSERT INTO movimentacoes (produto_id, tipo, quantidade, data)
    VALUES (?, ?, ?, ?)
    """, (produto_id, "entrada", quantidade, datetime.now()))

    conn.commit()
    conn.close()


def saida_estoque(produto_id, quantidade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade - ?
    WHERE id = ?
    """, (quantidade, produto_id))

    cursor.execute("""
    INSERT INTO movimentacoes (produto_id, tipo, quantidade, data)
    VALUES (?, ?, ?, ?)
    """, (produto_id, "saida", quantidade, datetime.now()))

    conn.commit()
    conn.close()


def historico():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movimentacoes ORDER BY data DESC")
    dados = cursor.fetchall()

    conn.close()
    return dados
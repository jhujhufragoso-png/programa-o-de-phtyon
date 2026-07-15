import sqlite3

# 1. Conexão com o Banco de Dados
def conectar():
    return sqlite3.connect("projeto.db")

def criar_tabela():
    """Cria a tabela no banco de dados se não existir."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# --- FUNÇÕES DO CRUD ---

# CREATE (Criar / Inserir)
def criar_item(nome, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO itens (nome, quantidade, preco)
        VALUES (?, ?, ?)
    """, (nome, quantidade, preco))
    conn.commit()
    conn.close()

# READ (Ler / Listar Todos)
def listar_itens():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM itens")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# UPDATE (Atualizar / Alterar)
def atualizar_item(id_item, novo_nome, nova_quantidade, novo_preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE itens
        SET nome = ?, quantidade = ?, preco = ?
        WHERE id = ?
    """, (novo_nome, nova_quantidade, novo_preco, id_item))
    conn.commit()
    conn.close()

# DELETE (Deletar / Remover)
def deletar_item(id_item):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM itens WHERE id = ?", (id_item,))
    conn.commit()
    conn.close()

# Inicializa o banco ao rodar o script
if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados pronto para uso!")
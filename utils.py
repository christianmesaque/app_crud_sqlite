import sqlite3


def conectar():
    conn = sqlite3.connect('psqlite3.db')

    conn.execute("""CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTERGER NOT NULL);
    """)
    return conn


def desconectar(conn):
    conn.close()


def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos...')
        print('__' * 10)
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('__' * 10)
    else:
        print('Não existem produtos cadastrados.')
    desconectar(conn)


def inserir():
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('informe a quantidade em estoque: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Não foi possível inserir o produto.')
    desconectar(conn)


def atualizar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('informe a quantidade em estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto com {nome} foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)


def deletar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))

    cursor.execute(f"DELETE FROM produtos WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto excluído com sucesso.')
    else:
        print('Erro ao excluir produto.')
    desconectar(conn)

def menu():
    
    print('==' *10, 'Gerenciamento de Produtos', '==' *10)
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos')
    print('3 - Atualizar produtos')
    print('4 - Deleter produto')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida.')
    else:
        print('Opção inválida.')
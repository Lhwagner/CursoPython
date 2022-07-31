import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# with conexao.cursor() as cursor:
#     sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#           '(%s, %s, %s, %s)'
#     cursor.execute(sql, ('Wagner', 'Wagner', 20, 98))
#     conexao.commit()

# with conexao.cursor() as cursor:
#     sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#           '(%s, %s, %s, %s)'
#
#     dados = [
#         ('LUCAO','WAGNER', 19, 97),
#         ('JONAS', 'WAGNER', 19, 97),
#         ('NON', 'WAGNER', 19, 97),
#     ]
#
#     cursor.executemany(sql, dados)
#     conexao.commit()

# with conexao.cursor() as cursor:
#     sql = 'DELETE FROM clientes WHERE id = %s'
#     cursor.execute(sql, (10,))
#     conexao.commit()

with conexao.cursor() as cursor:
    sql = 'UPDATE clientes SET nome=%s WHERE id = %s'
    cursor.execute(sql, ('JOAONA',5))
    conexao.commit()

with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM CLIENTES')
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)

conexao.close()

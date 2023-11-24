# essa é a estrutura de um banco de dados
#baixa o banco, conecta com o banco criado

import sqlite3

# define a variável conexão
conexaobanco = sqlite3.connect('bancodedados')

cursor = conexaobanco.cursor()

#cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome VARCHAR(100) NOT NULL, email VARCHAR(100) UNIQUE NOT NULL, senha VARCHAR(20) NOT NULL)')

cursor.execute('INSERT INTO usuarios (id, nome, email, senha) VALUES (1, "administrador", "administrador@blog.com", "Mudar@123")')

# as informações só são enviadas quando chegar nesse comando
conexaobanco.commit()

# encerra o processo
conexaobanco.close 






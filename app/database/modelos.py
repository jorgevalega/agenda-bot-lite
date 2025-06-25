# app/database/modelos.py

from app.database.conexao import obter_conexao

def criar_tabelas():
    conn = obter_conexao()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        telefone VARCHAR(20) UNIQUE,
        nome VARCHAR(100),
        tipo ENUM('free', 'vip', 'suspenso') DEFAULT 'free',
        data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario_id INT,
        descricao TEXT,
        data_hora DATETIME,
        criada_em DATETIME DEFAULT CURRENT_TIMESTAMP,
        notificada BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

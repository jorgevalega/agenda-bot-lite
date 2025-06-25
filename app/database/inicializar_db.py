# app/database/inicializar_db.py

from app.database.modelos import criar_tabelas

if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados inicializado com sucesso.")

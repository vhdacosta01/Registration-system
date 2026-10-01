import sqlite3
from werkzeug.security import check_password_hash

def get_connection():
    return sqlite3.connect("database.db")


def init_database():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()


def insert_user(name, email, password):
    print("ENTROU NO INSERT_USER")

    con = get_connection()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO usuarios (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )

    con.commit()

    cur.execute("SELECT * FROM usuarios")
    print("USUÁRIOS NO BANCO:", cur.fetchall())

    con.close()

def login_attempt(email, password):
    print("Entrou no login_attempt")

    con = get_connection()
    cur = con.cursor()

    cur.execute(
        "SELECT * FROM usuarios WHERE email = ?",
        (email,)
    )

    usuario = cur.fetchone()

    if usuario:
        senha_banco = usuario[3]

        
        if check_password_hash(senha_banco, password):
            print("Login correto")
            con.close()
            return True
        else:
            print("Senha incorreta")
            con.close()
            return False

    print("Usuário não encontrado")
    con.close()
    return False
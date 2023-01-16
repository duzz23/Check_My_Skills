import sqlite3
# Создание таблици
DB_FILENAME = 'db.sqlite3'

def main():
    sql_create_table = '''
    CREATE TABLE IF NOT EXISTS autors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR UNIQUE NOT NUlL,
        email VARCHAR UNIQUE
    );
    '''

    con = sqlite3.connect(DB_FILENAME)
    cur = con.cursor()
    cur.execute(sql_create_table)

# Заполнение таблици в ручную

    username = 'andrey'
    email = None

    cur.execute(
        """
        INSERT INTO autors(username, email)
        VALUES (?, ?);
        """,
        (username, email),
    )
    con.commit()
    con.close()





if __name__ == "__main__":
    main()
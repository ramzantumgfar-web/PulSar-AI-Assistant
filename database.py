import sqlite3


DB = "database.db"


def connect():
    return sqlite3.connect(DB)


def setup():

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        messages INTEGER DEFAULT 0
    )
    """)

    db.commit()
    db.close()


def add_user(user_id, username):

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (id, username)
        VALUES (?, ?)
        """,
        (
            user_id,
            username
        )
    )

    db.commit()
    db.close()


def add_message(user_id):

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE users
        SET messages = messages + 1
        WHERE id = ?
        """,
        (user_id,)
    )

    db.commit()
    db.close()


def users_count():

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    count = cursor.fetchone()[0]

    db.close()

    return count

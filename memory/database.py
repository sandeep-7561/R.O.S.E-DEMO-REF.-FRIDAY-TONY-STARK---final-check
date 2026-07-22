import sqlite3

connection = sqlite3.connect(
    "rose.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    key TEXT UNIQUE,

    value TEXT

)
""")

connection.commit()


def save_memory(key, value):

    cursor.execute(
        """
        INSERT OR REPLACE INTO memory(key, value)
        VALUES(?, ?)
        """,
        (key, value)
    )

    connection.commit()


def get_memory(key):

    cursor.execute(
        """
        SELECT value
        FROM memory
        WHERE key = ?
        """,
        (key,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return None


def delete_memory(key):

    cursor.execute(
        """
        DELETE FROM memory
        WHERE key = ?
        """,
        (key,)
    )

    connection.commit()
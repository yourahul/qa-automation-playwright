import sqlite3


def test_user_exists_in_db():
    conn = sqlite3.connect("test_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'Rahul')")
    conn.commit()

    cursor.execute("SELECT * FROM users WHERE name='Rahul'")
    result = cursor.fetchone()

    conn.close()

    assert result is not None

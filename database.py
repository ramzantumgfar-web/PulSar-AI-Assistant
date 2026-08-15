def add_balance(user_id, amount):
    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE id = ?",
        (amount, user_id)
    )
    conn.commit()


def get_balance(user_id):
    cursor.execute(
        "SELECT balance FROM users WHERE id = ?",
        (user_id,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return 0

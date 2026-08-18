def get_user(username):
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
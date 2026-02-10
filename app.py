from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = "database.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE email = '" + email + "' AND password = '" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify({"status": "ok", "user_id": user[0], "is_admin": user[4]})
    else:
        return jsonify({"status": "error"}), 401


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

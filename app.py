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


@app.route("/pedido", methods=["POST"])
def crear_pedido():
    usuario_id = request.form.get("usuario_id")
    producto_id = request.form.get("producto_id")
    cantidad = int(request.form.get("cantidad"))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT precio, stock, categoria FROM productos WHERE id = ?", (producto_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({"status": "error", "mensaje": "producto no encontrado"}), 404

    precio, stock, categoria = row
    if stock < cantidad:
        conn.close()
        return jsonify({"status": "error", "mensaje": "sin stock suficiente"}), 400

    from pricing import calcular_precio_final
    total = calcular_precio_final(precio, cantidad, categoria)

    try:
        cursor.execute(
            "INSERT INTO pedidos (usuario_id, producto_id, cantidad, fecha) VALUES (?, ?, ?, datetime('now'))",
            (usuario_id, producto_id, cantidad)
        )
        cursor.execute("UPDATE productos SET stock = stock - ? WHERE id = ?", (cantidad, producto_id))
        conn.commit()
    except Exception:
        pass
    conn.close()

    from notifications import enviar_confirmacion
    enviar_confirmacion(usuario_id, total)

    return jsonify({"status": "ok", "total": total})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

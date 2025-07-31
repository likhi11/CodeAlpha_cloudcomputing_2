from flask import Flask, request, jsonify
from utils.encryption import encrypt_data, decrypt_data
from utils.db import init_db, safe_query
import os

app = Flask(__name__)
db_conn = init_db()

# Capability code - like an access token
CAPABILITY_CODE = os.getenv("CAPABILITY_CODE", "secure123")

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if data.get("code") != CAPABILITY_CODE:
        return jsonify({"error": "Unauthorized"}), 403

    username = encrypt_data(data.get("username"))
    password = encrypt_data(data.get("password"))
    safe_query(db_conn, "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    return jsonify({"status": "User added securely"}), 200

@app.route("/get_users", methods=["GET"])
def get_users():
    users = safe_query(db_conn, "SELECT username, password FROM users", fetch=True)
    decrypted_users = [{"username": decrypt_data(u[0]), "password": decrypt_data(u[1])} for u in users]
    return jsonify(decrypted_users)

if __name__ == "__main__":
    app.run(debug=True)
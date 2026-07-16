from flask import Flask, render_template, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)

APP_VERSION = "1.0.0"


def get_connection():
    for _ in range(10):
        try:
            return mysql.connector.connect(
                host=os.getenv("MYSQL_HOST", "mysql"),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", "root"),
                database=os.getenv("MYSQL_DB", "devops")
            )
        except Exception:
            time.sleep(2)

    return None


@app.route("/")
def home():

    conn = get_connection()

    if conn is None:
        return "Database Connection Failed"

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")

    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", messages=messages)


@app.route("/api/messages")
def api_messages():

    conn = get_connection()

    if conn is None:
        return jsonify({"error": "Database Connection Failed"}), 500

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM messages")

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


@app.route("/health")
def health():

    return jsonify({
        "status": "UP"
    })


@app.route("/version")
def version():

    return jsonify({
        "application": "Two-Tier Flask CI/CD",
        "version": APP_VERSION,
        "author": "Revanth BL"
    })


@app.route("/metrics")
def metrics():

    conn = get_connection()

    database = "Connected" if conn else "Disconnected"

    if conn:
        conn.close()

    return jsonify({
        "application": "Running",
        "database": database,
        "status": "Healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
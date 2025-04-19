from flask import Flask, jsonify, request
import requests
import sqlite3
import traceback

ESP32_IP = "http://192.168.15.111"  # Use the ESP32 IP in your local network 

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('sensor_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            humidity REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/saveData", methods=["GET"])
def save_data():
    try:
        response = requests.get(f"{ESP32_IP}/getValues")
        data = response.json()

        temp = data[0]["value"]
        hum = data[1]["value"]

        conn = sqlite3.connect('sensor_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO sensor_data (temperature, humidity) VALUES (?, ?)", (temp, hum))
        conn.commit()
        conn.close()

        return jsonify({"status": "ok", "temperature": temp, "humidity": hum})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route("/insecure")
def insecure():
    temperature = request.args.get("temperature", "")
    
    # SQL injection point
    query = f"SELECT * FROM sensor_data WHERE temperature = '{temperature}'"
    
    conn = sqlite3.connect("sensor_data.db")
    c = conn.cursor()
    try:
        print(f"[DEBUG] Executing query: {query}")
        c.execute(query)
        rows = c.fetchall()
    except Exception as e:
        return traceback.format_exc()
    finally:
        conn.close()

    result = ""
    for row in rows:
        result += f"{row}<br>"
    
    return result or "Any result found."

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
# Database API

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![SQLlite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white)](https://sqlite.org/)


<h4 align="left"> 
	Author ✏️: <a href="https://github.com/GabrielPivoto">Pivoto 👽</a>
</h4>

### What is needed 🧾
- [x] [ESP32 application must be running](https://github.com/iotframeworkinatel/rest_api_esp32)
- [x] [Python](https://www.python.org/downloads/)

---
### Initial Configuration 🔧

- Clone the repository:

```
https://github.com/iotframeworkinatel/database-api.git
```
- Install Flask (on the root directory):
```
pip install flask
```

- Change ESP32 IP adress to the one in your local network. For instance, in **api.py**, set the IP adress:
```
ESP32_IP = "http://192.168.15.111"
```

### Run the application ▶️

- On the root directory, run the command:
```
python api.py
```

The application should start running on port 5000

### How it works ⚙️

This API is designed to read data from an ESP32 device and store it in a SQLite database. It exposes two GET endpoints:

- /saveData: Fetches sensor data from the ESP32 and saves it to the database.

- /insecure: A deliberately vulnerable endpoint created to expose an SQL injection entry point for security scanning purposes. It accepts a temperature parameter via the query string, which is directly used in an SQL statement without sanitization.
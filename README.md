# IoT Security Scanners🛡️


<h4 align="left"> 
	Author ✏️: <a href="https://github.com/GabrielPivoto">Pivoto 👽</a>
</h4>

---

### 🧭 Project Structure

This repository contains the code for three interconnected applications:

- **`esp32-rest-api/`**: Microcontroller-side REST API running on ESP32, responsible for reading temperature and humidity using a DHT11 sensor.
- **`front-end/`**: React + Tailwind web interface that consumes the ESP32 API and displays sensor data.
- **`database-api/`**: A Flask-based backend API that stores data into a database and contains an intentionally vulnerable SQL endpoint for testing security scanners.

Each folder contains its own `README.md` with step-by-step instructions for configuration and execution.

---

### 🔐 Security Testing with Nikto & Wapiti

The following tools can be used to scan the applications for vulnerabilities:

#### ▶️ Running **Nikto**

Nikto is an open-source web server scanner that performs comprehensive tests against web servers to identify potential security issues. It checks for over 6,700 potentially dangerous files and programs, outdated server software, and other common vulnerabilities.

**Command format:**
```bash
nikto -h http://<IP_or_HOST>:<PORT>
```

#### ▶️ Running **Wapiti**

Wapiti is a powerful web application vulnerability scanner that crawls a website to find attack surfaces and test them for common vulnerabilities like SQL Injection, XSS (Cross-site Scripting), Command Injection, File Disclosure, and more.

**Command format:**
```bash
wapiti -u http://<IP_or_HOST>:<PORT>/<endpoint> --flush-session
```
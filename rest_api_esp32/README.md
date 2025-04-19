# ESP32 REST API

[![ESP32](https://img.shields.io/badge/-ESP32-000?style=for-the-badge&logo=espressif)](https://www.espressif.com/)
[![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)](https://www.arduino.cc/)
[![WiFiManager](https://img.shields.io/badge/WiFiManager-E34F26?style=for-the-badge&logo=wifi&logoColor=white)](https://github.com/tzapu/WiFiManager)

<h4 align="left"> 
	Author ✏️: <a href="https://github.com/GabrielPivoto">Pivoto 👽</a>
</h4>

---

### What is needed 🧾

- [x] ESP32
- [x] DHT11 Sensor
- [x] Arduino IDE (or PlatformIO)
- [x] WiFiManager library
- [x] ArduinoJson library

---

### Setup & Flashing ⚙️

1. Clone this repository or copy the code to your Arduino project.
2. Install the required libraries:
   - `WiFiManager`
   - `DHT sensor library`
   - `DHTesp`
   - `ArduinoJson`
3. Connect the components to the ESP32:
   - DHT11 data pin to GPIO 18
   - LED PWM to GPIO 16
   - Boolean LED to GPIO 15
4. Flash the code using the Arduino IDE or PlatformIO.

When booting up for the first time, the ESP32 will start a Wi-Fi Access Point named `AutoConnectAP` (password: `password`). Connect to it and configure your Wi-Fi credentials via the browser.

---

### How it works 🚀

- The ESP32 connects to your local Wi-Fi network using **WiFiManager**.
- It reads **temperature and humidity** from a **DHT11 sensor** every few seconds.
- It exposes a REST API with two main endpoints:
  - `GET /getValues`: returns a JSON containing temperature, humidity, and LED statuses.
  - `POST /setStatus`: accepts a JSON with `led1Status` (PWM %) and `led2Status` (boolean) to control the LEDs.
- The data can be consumed by any front-end or client via HTTP requests.

---

### Endpoints 📡

#### 🔹 `GET /getValues`

**Example response:**
```json
[
  { "name": "temperature", "value": 23.5, "unit": "°C" },
  { "name": "humidity", "value": 55.2, "unit": "%" },
  { "name": "led1Status", "value": 128, "unit": "%" },
  { "name": "led2Status", "value": true, "unit": "boolean" }
]
```

#### 🔹 `POST /setStatus`

**Example request body:**
```json
{
  "led1Status": 200,
  "led2Status": true
}
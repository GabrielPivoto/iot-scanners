# Front-end

[![React](https://img.shields.io/badge/-ReactJs-61DAFB?logo=react&logoColor=white&style=for-the-badge)](https://react.dev/)
[![Tailwind](https://img.shields.io/badge/tailwindcss-0F172A?&logo=tailwindcss)](https://tailwindcss.com/)
[![Node js](https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white)](https://nodejs.org/en)


<h4 align="left"> 
	Author ✏️: <a href="https://github.com/GabrielPivoto">Pivoto 👽</a>
</h4>

### What is needed 🧾
- [x] [ESP32 application must be running](https://github.com/iotframeworkinatel/rest_api_esp32)
- [x] [Node js](https://nodejs.org/en)

---
### Initial Configuration 🔧

- Clone the repository:

```
https://github.com/iotframeworkinatel/front-end.git
```
- Install the dependencies (on the root directory):
```
npm install 
```
or
```
npm i
```

- Change ESP32 IP adress to the one in your local network. For instance, in **vite.config.js**, set the IP adress:
```
 target: 'http://192.168.15.111'
```


### Run the application ▶️

- On the root directory, run the command:
```
npm run dev
```

The application should start running on port 5173 or the next one available 

### How it works ⚙️

The front-end provides a button that, when clicked, sends a GET request to the REST API running on the ESP32. The API responds with the temperature and humidity values read from the DHT11 sensor, which are then displayed on the screen.
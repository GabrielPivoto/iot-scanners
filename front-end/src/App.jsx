import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [temperature, setTemperature] = useState('--')
  const [humidity, setHumidity] = useState('--')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const fetchData = async () => {
    setLoading(true)
    setError(null)
    
    try {
      // Usando o proxy configurado no Vite
      const response = await axios.get('/api/getValues')
      
      const temperatureObj = response.data.find(item => item.name === 'temperature')
      const humidityObj = response.data.find(item => item.name === 'humidity')
      
      if (temperatureObj) {
        setTemperature(`${temperatureObj.value.toFixed(1)} ${temperatureObj.unit}`)
      }
      
      if (humidityObj) {
        setHumidity(`${humidityObj.value} ${humidityObj.unit}`)
      }
    } catch (err) {
      setError(err.response?.data?.message || err.message)
      console.error('Error:', {
        config: err.config,
        response: err.response,
        stack: err.stack
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <h1>Sensor values</h1>
      
      <button 
        onClick={fetchData} 
        disabled={loading}
        className={`fetch-button ${loading ? 'loading' : ''}`}
      >
        {loading ? 'Loading...' : 'Get values'}
      </button>
      
      {error && <p className="error">Error: {error}</p>}
      
      <div className="data-container">
        <div className="data-card">
          <h2>Temperature</h2>
          <p>{temperature}</p>
        </div>
        
        <div className="data-card">
          <h2>Umidity</h2>
          <p>{humidity}</p>
        </div>
      </div>
    </div>
  )
}

export default App
import { useState, useEffect } from 'react'
import Projects from './components/ProjectsList'
import "./stylesheet.css"

function App() {

  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

useEffect(() => {
  fetch('/profile')
  .then((response) => response.json())
  .then((data) => {setLoading(false)
    setProfileData({
      profile_name: data.name,
      about_me: data.about
      })
    }
  )
  .catch((error) => {
    if (error.response) {
      console.log(error.response)
      console.log(error.response.status)
      console.log(error.response.headers)
      }
    }
  )
}, [])

  return (
    <>
      <div className="App">
        {loading && <p>Loading...</p>}
        {!loading && <p>{ profileData.about_me }</p>}
      </div>
    </>
  )
}

export default App;
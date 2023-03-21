import { useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Projects from './components/ProjectsList'
import Auth from './components/Auth'
import 'bootstrap/dist/css/bootstrap.min.css'
import './stylesheet.css'
import SignIn from './components/SignIn'
import SignUp from './components/SignUp'

function App() {

  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

function getProfile() {
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
}

  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/view-projects" element={<Projects/>} />
        <Route exact path="/sign-in" element={<SignIn/>} />
        <Route exact path="/sign-up" element={<SignUp/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
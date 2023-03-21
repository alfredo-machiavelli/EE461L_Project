import React, { useState } from "react";
export default function (props) {

  const [authMode, setAuthMode] = useState("signin");
  const [formData, setFormData] = useState({
    fullName: "",
    username: "",
    password: ""
  })

  const changeAuthMode = () => {
    setAuthMode(authMode === "signin" ? "signup" : "signin");
  };

  function pushData(e) {
    e.preventDefault()

    let fd = new FormData()
    fd.append('Full Name', formData.fullName)
    fd.append('Username', formData.username)
    fd.append('Password', formData.password)

    fetch('/auth', {
      method: 'POST',
      body: fd
    })
    e.target.fullName = ""
    e.target.username = ""
    e.target.password = ""

    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.log(err))
  }

  function handle(e) {
    const newData = {...formData}
    newData[e.target.id] = e.target.value
    setFormData(newData)
  }

  if (authMode === "signin") {
    return (
      <div className="Auth-form-container">
        <form className="Auth-form" onSubmit={(e) => pushData(e)}>
          <div className="Auth-form-content">
            <h3 className="Auth-form-title">Sign In</h3>
            <div className="text-center">
              Not registered yet?{" "}
              <span className="link-primary" onClick={changeAuthMode}>
                Sign Up
              </span>
            </div>
            <div className="form-group mt-3">
              <label>Username</label>
              <input
                onChange={(e) => handle(e)}
                id="username"
                type="text"
                className="form-control mt-1"
                placeholder="Enter username"
              />
            </div>
            <div className="form-group mt-3">
              <label>Password</label>
              <input
                onChange={(e) => handle(e)}
                id="password"
                type="password"
                className="form-control mt-1"
                placeholder="Enter password"
              />
            </div>
            <div className="d-grid gap-2 mt-3">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
            <p className="text-center mt-2">
              Forgot <a href="#">password?</a>
            </p>
          </div>
        </form>
      </div>
    );
  } else {
    return (
      <div className="Auth-form-container">
        <form className="Auth-form" onSubmit={(e) => pushData(e)}>
          <div className="Auth-form-content">
            <h3 className="Auth-form-title">Sign In</h3>
            <div className="text-center">
              Already registered?{" "}
              <span className="link-primary" onClick={changeAuthMode}>
                Sign In
              </span>
            </div>
            <div className="form-group mt-3">
              <label>Full Name</label>
              <input
                onChange={(e) => handle(e)}
                id="fullName"
                type="text"
                className="form-control mt-1"
                placeholder="e.g Jane Doe"
              />
            </div>
            <div className="form-group mt-3">
              <label>Username</label>
              <input
                onChange={(e) => handle(e)}
                id="username"
                type="text"
                className="form-control mt-1"
                placeholder="Username"
              />
            </div>
            <div className="form-group mt-3">
              <label>Password</label>
              <input
                onChange={(e) => handle(e)}
                id="password"
                type="password"
                className="form-control mt-1"
                placeholder="Password"
              />
            </div>
            <div className="d-grid gap-2 mt-3">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
            <p className="text-center mt-2">
              Forgot <a href="#">password?</a>
            </p>
          </div>
        </form>
      </div>
    );
  }
}

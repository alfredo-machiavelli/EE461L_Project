import React, { useState } from "react";
export default function (props) {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  function pushData(e) {
    e.preventDefault();

    let fd = new FormData();
    fd.append("Username", formData.username);
    fd.append("Password", formData.password);

    fetch("/auth", {
      method: "POST",
      body: fd,
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((err) => console.log(err));
  }

  function handle(e) {
    const newData = { ...formData };
    newData[e.target.id] = e.target.value;
    setFormData(newData);
  }

  return (
    <div className="Auth-form-container">
      <form className="Auth-form" onSubmit={(e) => pushData(e)}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign In</h3>
          <div className="text-center">
            Not registered yet?{" "}
            <a className="link-primary" href="/sign-up">
              Sign Up
            </a>
          </div>
          <div className="form-group mt-3">
            <label>Username</label>
            <input
              onChange={(e) => handle(e)}
              id="username"
              type="text"
              className="form-control mt-1"
              placeholder="Enter username"
              required
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
              required
            />
          </div>
          <div className="text-center mt-2">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}

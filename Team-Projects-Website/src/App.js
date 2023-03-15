import React, { Component } from "react";
import Projects from "./components/Projects";

import './stylesheet.css'

class App extends Component {
  render() {
    return (
      <div className="container">
          <Projects/>
      </div>
    );
  }
}
export default App;
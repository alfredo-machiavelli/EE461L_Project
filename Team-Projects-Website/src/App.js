import React, { Component } from "react";
import ProjectsList from "./components/ProjectsList";

import './stylesheet.css'

class App extends Component {
  render() {
    return (
      <div className="column">
          <ProjectsList/>
      </div>
    );
  }
}
export default App;
import React, { Component } from 'react'

export default class ProjectName extends Component {
  render() {
    return (
      <div className='projName'>
        <h3>{ this.props.name }</h3>
      </div>
    )
  }
}

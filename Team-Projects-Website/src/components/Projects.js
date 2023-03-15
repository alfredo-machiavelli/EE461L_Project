import React, { Component } from 'react'
import Project from './Project.js'

export default class Projects extends Component {
  render() {
    const list = 'list, of, authorized, users';
    return (
      <div className='projects'>
        <h1>Projects</h1>
        <Project name = 'Project Name 1' authUsers = { list } HWSet1Qty = '50' HWSet2Qty = '0' JoinOrLeave = 'Join'/>
        <Project name = 'Project Name 2' authUsers = { list } HWSet1Qty = '50' HWSet2Qty = '0' JoinOrLeave = 'Leave'/>
        <Project name = 'Project Name 3' authUsers = { list } HWSet1Qty = '0' HWSet2Qty = '0' JoinOrLeave = 'Join'/>
      </div>
    )
  }
}

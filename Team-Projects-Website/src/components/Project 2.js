import React, { Component } from 'react'
import ProjectName from "./ProjectName";
import AuthUserList from "./AuthUserList";
import CheckInOut from "./CheckInOut";

export default class Projects extends Component {
  render() {
    return (
      <div className='project'>
        <ProjectName name = { this.props.name }/>
        <AuthUserList authUsers = { this.props.authUsers }/>
        <CheckInOut HWSet1Qty = { this.props.HWSet1Qty } HWSet2Qty = { this.props.HWSet2Qty }/>
      </div>
    )
  }
}

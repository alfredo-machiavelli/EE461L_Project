import React, { Component } from 'react'

export default class AuthUserList extends Component {
  render() {
    return (
      <div className='authUsers'>
        { this.props.authUsers }
      </div>
    )
  }
}

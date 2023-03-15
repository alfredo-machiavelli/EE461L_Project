import React, { useState, useRef } from 'react'

function CheckInOut() {
  const [HWSet1Qty, setHWSet1Qty] = useState(0)
  const [HWSet2Qty, setHWSet2Qty] = useState(0)
  const [JoinedText, setJoinedText] = useState('Join')
  const [JoinedStatus, setJoinedStatus] = useState(false)

  const HWSet1Input = useRef()
  const HWSet2Input = useRef()

  function CheckInHWSet1(e) {
    if(JoinedStatus === true) {
    const input = HWSet1Input.current.value
    setHWSet1Qty(Number(HWSet1Qty) + Number(input))
    HWSet1Input.current.value = null
    } else {
      HWSet1Input.current.value = null
    }
  }

  function CheckOutHWSet1(e) {
    if(JoinedStatus === true) {
    const input = HWSet1Input.current.value
    setHWSet1Qty(Number(HWSet1Qty) - Number(input))
    HWSet1Input.current.value = null
    } else {
      HWSet1Input.current.value = null
    }
  }
  
  function CheckInHWSet2(e) {
    if(JoinedStatus === true) {
      const input = HWSet2Input.current.value
      setHWSet2Qty(Number(HWSet2Qty) + Number(input))
      HWSet2Input.current.value = null
    } else {
      HWSet2Input.current.value = null
    }
  }

  function CheckOutHWSet2(e) {
    if(JoinedStatus === true) {
      const input = HWSet2Input.current.value
      setHWSet2Qty(Number(HWSet2Qty) - Number(input))
      HWSet2Input.current.value = null
    } else {
      HWSet2Input.current.value = null
    }
  }

  function updateJoinedStatus(e) {
    if (JoinedText === 'Join') {
      setJoinedText('Leave')
    } else {
      setJoinedText('Join')
    }
    setJoinedStatus(!JoinedStatus)
  }

  return (
    <>
      <div className='hwSetsAndJoin'>
        <div className='hwSets'>
          <div className='hwSet'>
            <div className='quantity'>
              <div className='column'>
              <h3>HWSet1:</h3>
              <h3> { HWSet1Qty }/100</h3>
              </div>
            </div>
            <div className='enterQty'>
            <input ref={HWSet1Input} type='text' disabled={`${ JoinedStatus ? '' : 'disabled' }`} placeholder='             Enter Qty'/>
            </div>
            <div className='check'>
              <button onClick={CheckInHWSet1} type="button" className="btn btn-secondary">Check In</button>
            </div>
            <div className='check'>
            <button onClick={CheckOutHWSet1} type="button" className="btn btn-secondary">Check Out</button>
            </div>
          </div>

          <div className='hwSet'>
            <div className='quantity'>
              <div className='column'>
                <h3>HWSet2:</h3>
                <h3> { HWSet2Qty }/100</h3>
              </div>
            </div>
            <div className='enterQty'>
            <input ref={HWSet2Input} type='text' disabled={`${ JoinedStatus ? '' : 'disabled' }`} placeholder='             Enter Qty'/>
            </div>
            <div className='check'>
              <button onClick={CheckInHWSet2} type="button" className="btn btn-secondary">Check In</button>
            </div>
            <div className='check'>
            <button onClick={CheckOutHWSet2} type="button" className="btn btn-secondary">Check Out</button>
            </div>
          </div>
        </div>

        <button onClick={updateJoinedStatus} type="button" className={`btn  ${ JoinedStatus ? "btn-danger" : "btn-success" }`}>{ JoinedText }</button>

      </div>
    </>
  )
}

export default CheckInOut;

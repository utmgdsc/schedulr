import FullCalendar, { whenTransitionDone } from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin! 
import timeGridPlugin from '@fullcalendar/timegrid';
import "./calendar.css"
import React, {useState, useEffect, useContext} from 'react'

import { list1, list2, list3 } from './temp';
import AuthContext from '../context/AuthContext';

const Calendar2 = () => {
   // calendarRef = React.useRef()
    let {events, getEvents} = useContext(AuthContext);
    console.log("this is events")
    console.log(events)


  return (
    <div className="calendar">

<button onClick={getEvents}>
      Generate
    </button>
            <FullCalendar
            plugins={[ timeGridPlugin, dayGridPlugin ]}
            //ref= {calendarRef}
            initialView="timeGridWeek"
            slotMinTime={'08:00'}
            slotMaxTime= {'20:00'}
            weekends={true}
            allDaySlot={false}
            slotDuration={"01:00:00"}
            events= {events}
            
            displayEventTime = {true}
            
            headerToolbar={
              {center: 'dayGridMonth, timeGridWeek, timeGridDay', 

          }}
          
          expandRows={true}
            height = {'80vh'}
            
            //dayHeaderFormat={}
            
            />
            
        </div>
  )
}

export default Calendar2
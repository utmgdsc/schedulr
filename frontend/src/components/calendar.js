import FullCalendar, { whenTransitionDone } from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin! 
import timeGridPlugin from '@fullcalendar/timegrid';
import "./calendar.css"
import React, {useState, useEffect, useContext} from 'react'

import AuthContext from '../context/AuthContext';

const Calendar2 = () => {
   // calendarRef = React.useRef()
    let {events} = useContext(AuthContext);


  return (
    <div className="calendar">

            <FullCalendar
            plugins={[ timeGridPlugin, dayGridPlugin ]}
            //ref= {calendarRef}
            initialView="timeGridWeek"
            slotMinTime={'08:00'}
            slotMaxTime= {'20:00'}
            weekends={false}
            allDaySlot={false}
            slotDuration={"01:00:00"}
            events={events}
            // set start to january 1st 2023
            //start={new Date(2023, 0, 1)}
            displayEventTime = {true}
            // headerToolbar={
            //     {right: 'dayGridMonth, timeGridWeek, timeGridDay', 
            //     center: 'add'    
            // }}
            height = {'auto'}
            
            //dayHeaderFormat={}
            
            />
            
        </div>
  )
}

export default Calendar2
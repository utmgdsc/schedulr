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
    </button>;
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
            //events={list3}
            // events = {[
            //   {date: "2022-11-30",
            //    title: "event 1",
            //   end:"2022-11-30T10:00:00",
            //   start: "2022-11-30T09:00:00",
            //     display: "block"},
            //   {date :  "2022-12-01",
            //       display :  "block",
            //       end:  "2022-12-01T15:00:00",
            //       start:"2022-12-01T14:00:00",
            //       title: "MAT135 L0101"
            //     }
            // ]}
            // set start to january 1st 2023
            //start={new Date(2023, 0, 1)}
            displayEventTime = {true}
            
            headerToolbar={
              {center: 'dayGridMonth, timeGridWeek, timeGridDay', 

          }}
          expandRows={true}
            height = {'auto'}
            
            //dayHeaderFormat={}
            
            />
            
        </div>
  )
}

export default Calendar2
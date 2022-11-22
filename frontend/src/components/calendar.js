import FullCalendar, { whenTransitionDone } from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin! 
import timeGridPlugin from '@fullcalendar/timegrid';
import "./calendar.css"
import React from 'react'

function Calendar(){

    
    // let calendarRef  = React.createRef
    // var btn = document.getElementById("month")
    // btn.addEventListener("click", changeToMonth)

    

    return(
        <div className="calendar">
            <button type='button' id='month'>Month</button>
            <FullCalendar
            plugins={[ timeGridPlugin ]}
            //ref= {calendarRef}
            initialView="timeGridWeek"
            slotMinTime={'08:00'}
            slotMaxTime= {'20:00'}
            weekends={false}
            allDaySlot={false}
            slotDuration={"01:00:00"}
            events={[
            { title: ' event 1', date: '2022-11-01', display: 'block', start: '2022-11-01T10:30:00' },
            { title: 'event 2', date: '2022-11-02' }
            ]}
            displayEventTime = {true}
            eventContent={renderEventContent}
            height = {'auto'}
            
            dayHeaderContent
            />
        </div>

    

    )
    // function changeToMonth(){
    //     let calendarApi = calendarRef.current.getApi()
    //     calendarApi.next()
    // }
    

    
    function renderEventContent(eventInfo) {
    
    
        return (
          <>
            <b>{eventInfo.timeText}</b>
            <i>{eventInfo.event.title}</i>
          </>
        )
      }
}



  
export default Calendar
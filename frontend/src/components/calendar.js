import FullCalendar, { whenTransitionDone } from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin! 
import timeGridPlugin from '@fullcalendar/timegrid';
import "./calendar.css"
import React from 'react'

// function Calendar(){



//     
        
    

    
//     function renderEventContent(eventInfo) {
    
    
//         return (
//           <>
//             <b>{eventInfo.timeText}</b>
//             <i>{eventInfo.event.title}</i>
//           </>
//         )
//       }
// }



  
export default class Calendar extends React.Component{

    calendarRef = React.createRef()

  render() {
    return(
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
            events={[
            { title: ' event 1', date: '2022-11-01', display: 'block', start: '2022-11-01T10:30:00' },
            { title: 'event 2', date: '2022-11-02' }
            ]}
            
            displayEventTime = {true}
            headerToolbar={
                {right: 'dayGridMonth, timeGridWeek, timeGridDay', 
                center: 'add'    
            }}
            height = {'auto'}
            
            //dayHeaderFormat={}
            
            />
            
        </div>

    

            )
  }

  someMethod() {
    let calendarApi = this.calendarRef.current.getApi()
    calendarApi.next()

    calendarApi.next()
    
  }

}
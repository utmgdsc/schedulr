import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext';

import './HomePage.css'
import NavBar from '../components/nav-bar.js'
import Footer from '../components/footer.js'
import Calendar from '../components/calendar.js'
import FullCalendar, { whenTransitionDone } from '@fullcalendar/react' // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin!
import { formatDate } from '@fullcalendar/react'

const HomePage = () => {
  
  
  let [note, setNotes] = useState([]);
  let {authTokens, logoutUser } = useContext(AuthContext);

  useEffect(() => {
getNotes();
  }, [])

  let getNotes = async () => {

    let response = await fetch('http://127.0.0.1:8000/api/notes',
    {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authTokens.access}`
    }})
    let data = await response.json();

    if(response.status === 200){
      setNotes(data);
  }else if(response.statusText == 'Unauthorized'){
    logoutUser();

  }

 
}
 
  return (
    <div className='Home'>
      
    <NavBar></NavBar>
    
    <div className='main-section'>
      <div className='header'>
        Last Name, First Name



      </div>
      
      <div className='calendar'>
        <Calendar>


        </Calendar>
      
      </div>

      
      <Footer>

      </Footer>
    </div>
    
    </div>


  )
}



export default HomePage
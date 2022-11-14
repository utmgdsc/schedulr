import React from 'react'
import './Home.css'
import NavBar from './components/nav-bar.js'
import Footer from './components/footer.js'
import Calendar from './components/calendar.js'
// import Button from 'react'


function Home() { // import the react calendar api, put in dummy data, keep track of what data needs to go in the calendar
  
  //material ui library
  // any ui's i install make a list
  return (
    
    <div className='Home'>
      
        <NavBar></NavBar>
        
        <div className='main-section'>
          <div className='header'>
            Last Name, First Name



          </div>
          
          <div className='calendar'>


          </div>

          
          <Footer>

          </Footer>
        </div>
        
      




      <div></div>


    </div>
    
    
    


  )
}

export default Home
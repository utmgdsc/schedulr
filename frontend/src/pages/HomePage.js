import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext';

import './HomePage.css'
import NavBar from '../components/nav-bar.js'
import Footer from '../components/footer.js'

import Calendar2 from '../components/calendar';


const HomePage = () => {
  let [note, setNotes] = useState([]);

  let {authTokens, logoutUser, user, getEvents } = useContext(AuthContext);

  useEffect(() => {
  getNotes();
  getEvents();
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
      console.log(data)
      console.log(user.username)
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
        {/* {user.last_name}, {user.first_name} */}

      </div>

        <Calendar2></Calendar2>

      
      <Footer></Footer>
    </div>
    
    </div>


  )
}

export default HomePage
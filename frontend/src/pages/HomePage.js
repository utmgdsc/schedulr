import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext';

import './HomePage.css'
import NavBar from '../components/nav-bar.js'
import Footer from '../components/footer.js'

import Calendar2 from '../components/calendar';


const HomePage = () => {
  let [note, setNotes] = useState([]);
  let {authTokens, logoutUser, user } = useContext(AuthContext);

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
 //razeen's prev code
  // return (
  //   <div>
  //      <ul>
  //       {note.map(note => (
  //         <li key={note.id}>{note.body}</li>
  //       ))}
  //       </ul>
  //   </div>
  // )
  return (
    <div className='Home'>
      
    <NavBar></NavBar>
    
    <div className='main-section'>
      <div className='header'>
        {/* {user.last_name}, {user.first_name} */}

      </div>
      
      <div className='calendar'>
        
        
        {/* <Calendar></Calendar> */}
        <Calendar2></Calendar2>

      </div>

      
      <Footer>

      </Footer>
    </div>
    
    </div>


  )
}

export default HomePage
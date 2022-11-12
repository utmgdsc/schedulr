import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext';


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
    <div>
       <ul>
        {note.map(note => (
          <li key={note.id}>{note.body}</li>
        ))}
        </ul>
    </div>
  )
}

export default HomePage
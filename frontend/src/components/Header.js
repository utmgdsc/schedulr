import React, {useContext} from 'react'
import { Link } from 'react-router-dom'
import  AuthContext  from '../context/AuthContext'


const Header = () => {
    let {user, logoutUser} = useContext(AuthContext);
  return (
    <div>
      
        <Link to="/">Home</Link>
        <span> | </span>
        { user ? (<p onClick={logoutUser}>Logout</p>): (<Link to="/login">Login</Link>)}

        <span> | </span>
        <Link to="register">Register</Link>
        
    </div>
  )
}

export default Header
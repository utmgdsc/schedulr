import React, {useContext} from 'react'
import { Link } from 'react-router-dom'
import  AuthContext  from '../context/AuthContext'
import './header.css'

const Header = () => {
    let {user, logoutUser} = useContext(AuthContext);
  return (
    <div className='header'>
      
        <Link to="/">Home</Link>
        <span> | </span>
        { user ? (<span></span>): (<Link to="/login">Login</Link>)}
        <span> | </span>
        <Link to="/userform">UserForm</Link>
        
        <span> | </span>
        <Link to="register">Register</Link>
        
    </div>
  )
}

export default Header
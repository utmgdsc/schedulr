import React, {useContext} from 'react'
import { Link } from 'react-router-dom'
import  AuthContext  from '../context/AuthContext'
import './header.css'

const Header = () => {
    let {user, logoutUser} = useContext(AuthContext);
    const linkStyle = {
      margin: "1rem",
      textDecoration: "none",
      color: 'white'
    };
    return (
    <div className='header'>
      
        <Link to="/" style={linkStyle}>Home</Link>
        <span> | </span>
        { user ? (<span></span>): (<Link to="/login" style={linkStyle}>Login</Link>)}
        <span> | </span>
        <Link to="/userform" style={linkStyle}>UserForm</Link>
        
        <span> | </span>
        <Link to="register" style={linkStyle}>Register</Link>
        <span> | </span>
        <span style={linkStyle}>{!user ? (<span></span>) :(<span>hii {user.username}</span>) } </span>
    </div>
  )
}

export default Header
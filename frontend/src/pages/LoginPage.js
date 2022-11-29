import React, {useContext} from 'react';
import Footer from '../components/footer';
import AuthContext from '../context/AuthContext';
import './LoginPage.css';

const LoginPage = () => {

    let {loginUser} = useContext(AuthContext);
  return (
    
    <div className="login-page">
        <div className="login-form">
          Please Enter your Username and Password
        
          <form onSubmit={loginUser}>
              <input type="text" name="username" placeholder='enter username' />
              <input type="password" name="password" placeholder='enter password' />
              <input type="submit" />
          </form>
        </div>
        <Footer/>
    </div>
  )
}

export default LoginPage
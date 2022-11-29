import React, {useContext} from 'react';
import AuthContext from '../context/AuthContext';
import './LoginPage.css'
import Footer from '../components/footer';

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
        <Footer></Footer>
    </div>
  )
}

export default LoginPage
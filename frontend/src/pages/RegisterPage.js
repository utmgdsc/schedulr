import React, {useContext} from 'react';
import Footer from '../components/footer';
import AuthContext from '../context/AuthContext';
import './RegisterPage.css'


const RegisterPage = () => {
    let {registerUser} = useContext(AuthContext);
  return (
    <div className='register-page'>
      <div className="register-form">
        <div className="inputs">
        
      
          <form onSubmit={registerUser} className='register-inputs'>
              {/* apply input fields for username, password, password, email, first name, last name */}
              RegisterPage <br/><br/>
              <label>UserName:
              <input type="text" name="username" placeholder='enter username' />
              </label>
              <br/>
              <label>Password:
              <input type="password" name="password" placeholder='enter password' />
              </label>

              <br/>
              <label>Confirm Password: 
              <input type="password" name="password2" placeholder='confirm password' />
              </label>

              <br/>
              <label>Email: 
              <input type="email" name="email" placeholder='enter email' />
              </label>

              <br/>
              <label>First Name:
              <input type="text" name="first_name" placeholder='enter first name' />
              </label>

              <label>Last Name:
              <input type="text" name="last_name" placeholder='enter last name' />
              </label>

              <br/>
              <label>
              <input type="submit" />
              </label>
          </form>
        </div>  
      </div>
    <Footer></Footer>
    </div>
  )
}

export default RegisterPage
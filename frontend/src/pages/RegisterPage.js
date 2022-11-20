import React, {useContext} from 'react';
import AuthContext from '../context/AuthContext';

const RegisterPage = () => {
    let {registerUser} = useContext(AuthContext);
  return (
    <div>RegisterPage <br/>
    <form onSubmit={registerUser}>
        {/* apply input fields for username, password, password, email, first name, last name */}
        <input type="text" name="username" placeholder='enter username' />
        <input type="password" name="password" placeholder='enter password' />
        <input type="password" name="password2" placeholder='confirm password' />
        <input type="email" name="email" placeholder='enter email' />
        <input type="text" name="first_name" placeholder='enter first name' />
        <input type="text" name="last_name" placeholder='enter last name' />
        <input type="submit" />

    </form>
    </div>
  )
}

export default RegisterPage
import { useContext } from 'react';
import './nav-bar.css'
import AuthContext from '../context/AuthContext';


function NavBar(){
    let {logoutUser} = useContext(AuthContext);

    return(
        <div className="nav-bar">
            
            <div className='logo'>Schedulr.</div>    

            <div id='courses-button' className='buttons'>Courses</div>
            <div id='settings-button' className='buttons'>Settings</div>
            <div id='Logout-button' onClick={logoutUser} className='buttons'>Log Out</div>

        </div>

    );
}

export default NavBar
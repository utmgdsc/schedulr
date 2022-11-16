import './nav-bar.css'

function NavBar(){


    return(
        <div className="nav-bar">
            
            <div className='logo'>Schedulr.</div>

            

            <div id='courses-button' className='buttons'>Courses</div>
            <div id='settings-button' className='buttons'>Settings</div>
            <div id='Logout-button' className='buttons'>Log Out</div>

        </div>

    );
}

export default NavBar
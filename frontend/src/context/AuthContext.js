import { createContext,useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';

import jwt_decode from "jwt-decode";

const AuthContext = createContext()

export default AuthContext;


export const AuthProvider = ({children}) => {

    
    let [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null);
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null);
    let [loading, setLoading] = useState(true);

    let [events, setEvents] = useState([]);


    const navigate = useNavigate();

    let getEvents = async () => {
        let respone = await fetch('http://127.0.0.1:8000/api/events/',{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authTokens.access}`
            }
        })
        let data = await respone.json();
        if (respone.status === 200){
            setEvents(data);
            console.log(data);
        }
    }

    let input108 = async () => {
        
        let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "CSC108",
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success');
        }else{
            //log the error
            console.log('error');
            console.log(respone);
        }
  }


  let input148 = async () => {
    let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "CSC148",
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success');
        }else{
            //log the error
            console.log('error');
            console.log(respone);
        }
  }

  let input107 = async () => {
    let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "STA107",
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success');
        }else{
            //log the error
            console.log('error');
            console.log(respone);
        }
  }

  let input137 = async () => {
    let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "MAT137",
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success');
        }else{
            //log the error
            console.log('error');
            console.log(respone);
        }
  }
  let input135 = async () => {
    let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "MAT135",
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success');
        }else{
            //log the error
            console.log('error');
            console.log(respone);
        }
    }
    let input136 = async () => {
        let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "MAT136",
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success');
        }else{
            //log the error
            console.log('error');
            console.log(respone);
        }
    }
    let input102 = async () => {
        let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "MAT102",
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success');
        }else{
            //log the error
            console.log('error');
            console.log(respone);
        }
    }

    

    let registerUser = async (e ) => {
        e.preventDefault();
        let respone = await fetch('http://127.0.0.1:8000/api/register/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: e.target.username.value, 
                password: e.target.password.value,
                 password2: e.target.password2.value, 
                 email: e.target.email.value,
                 first_name: e.target.first_name.value,
                 last_name: e.target.last_name.value})
        }
        )
        let data = await respone.json();
        console.log('data: ',data);
        if(respone.status === 201){
            navigate('/login');
        } else {
            alert(data.message);
        }

    }

    let loginUser = async (e ) => {
        e.preventDefault();
        let respone = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username: e.target.username.value, password: e.target.password.value})
         } )

         let data = await respone.json();
         console.log('data: ', data);

         if (respone.status === 200){
             setAuthTokens(data);
             setUser(jwt_decode(data.access));
             localStorage.setItem('authTokens', JSON.stringify(data));
             getEvents();   
             navigate('/');
         } else {
             alert('incorrect username or password');
         }
    }

    let logoutUser = () => {
        setAuthTokens(null);
        setUser(null);
        localStorage.removeItem('authTokens');
        navigate('/login');
    }

    let updateToken = async () => {
        console.log('update token called');
        let respone = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'refresh': authTokens.refresh?.refresh})
         } )

         let data = await respone.json();

         if (respone.status === 200){
             setAuthTokens(data);
             setUser(jwt_decode(data.access));
             localStorage.setItem('authTokens', JSON.stringify(data));
         } else {
             logoutUser();
         }

         if(loading){
             setLoading(false);
         }

    }

    let contextData = {
        user: user,
        authTokens: authTokens,
        loginUser: loginUser,
        logoutUser: logoutUser,
        registerUser: registerUser,
        events: events,
        input108: input108,
        input107: input107,
        input137: input137,
        input135: input135,
        input136: input136,
        input102: input102,
        input148: input148,

    }

    useEffect(() => {

        let FourMinutes = 4 * 60 * 1000;
       let interval = setInterval(() => {
            if (authTokens) {
                updateToken();
            }
         }, FourMinutes )
         return () => clearInterval(interval);

    }, [authTokens, loading])

    return (
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}
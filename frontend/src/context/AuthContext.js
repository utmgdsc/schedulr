import { createContext,useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';

import jwt_decode from "jwt-decode";

const AuthContext = createContext()

export default AuthContext;


export const AuthProvider = ({children}) => {

    
    let [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null);
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null);
    let [loading, setLoading] = useState(true);


    const navigate = useNavigate();

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
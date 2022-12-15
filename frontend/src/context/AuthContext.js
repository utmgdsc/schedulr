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
    // let selectionlec108 = ''; 
    // let selectionlec148 = ''; 
    // let selectionlec107 = ''; 
    // let selectionlec102 = ''; 
    // let selectionlec135 = ''; 
    // let selectionlec136 = ''; 
    // let selectiontut108 = ''; 
    // let selectiontut148 = ''; 
    // let selectiontut107 = ''; 
    // let selectiontut102 = ''; 
    // let selectiontut135 = ''; 
    // let selectiontut136 = ''; 
    




    const navigate = useNavigate();

    let setPreference = async(time, day_limit, time_limit) => {

        // if time is morning, set time_number to 0, if afternoon, set time_number to 1, if evening, set time_number to 2


        let respone = await fetch('http://127.0.0.1:8000/api/inputPreference/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                student_max_studytime: day_limit,
                student_time_pref: time,
                student_max_timeblock: time_limit,
    })})
    let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success 108');
        }else{
            //log the error
            console.log('error 108');
            console.log(respone);
        }
    }


    let getEvents = async () => {
        let respone = await fetch('http://127.0.0.1:8000/api/events/',{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json', 
                'Authorization': `Bearer ${authTokens.access}`
            }
        })
        let data = await respone.json();
        console.log("hey");
        console.log(authTokens.access + " yeahhh");
        if (respone.status === 200){
            console.log("success of getting events");
            setEvents(data);
            
            console.log(data);
        } else {
            alert('error');
        }
    }


    let input108 = async (selectionlec108, selectiontut108) => {
        console.log("!!!!---- this is my lec and tut value before api call ----!!!!")
        console.log(selectionlec108);
        console.log(selectiontut108);
        
        let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "CSC108",
                course_lec: selectionlec108,
                course_tut: selectiontut108,
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success 108');
        }else{
            //log the error
            console.log('error 108');
            console.log(respone);
        }
  }


  let input148 = async (selectionlec148, selectiontut148) => {
    let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "CSC148",
                course_lec: selectionlec148,
                course_tut: selectiontut148,
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success 148');
        }else{
            //log the error
            console.log('error 148');
            console.log(respone);
        }
  }

  let input107 = async (selectionlec107, selectiontut107) => {
    let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "STA107",
                course_lec: selectionlec107,
                course_tut: selectiontut107,
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success 107');
        }else{
            //log the error
            console.log('error 107');
            console.log(respone);
        }
  }

//   let input137 = async () => {
//     let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({
//                 custom_field: user.username,
//                 course: "MAT137",
//                 })
//         }
//         )
//        let data= await respone.json();
//         console.log(data);
//         if (respone.status === 200){
//             console.log('success');
//         }else{
//             //log the error
//             console.log('error');
//             console.log(respone);
//         }
//   }
  let input135 = async (selectionlec135, selectiontut135) => {
    let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "MAT135",
                course_lec: selectionlec135,
                course_tut: selectiontut135,
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success 135');
        }else{
            //log the error
            console.log('error 135');
            console.log(respone);
        }
    }
    let input136 = async (selectionlec136,selectiontut136) => {
        let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "MAT136",
                course_lec: selectionlec136,
                course_tut: selectiontut136,
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success 136');
        }else{
            //log the error
            console.log('error 136');
            console.log(respone);
        }
    }
    let input102 = async (selectionlec102, selectiontut102) => {
        let respone = await fetch('http://127.0.0.1:8000/api/inputCourse/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                custom_field: user.username,
                course: "MAT102",
                course_lec: selectionlec102,
                course_tut: selectiontut102,
                })
        }
        )
       let data= await respone.json();
        console.log(data);
        if (respone.status === 200){
            console.log('success 102');
        }else{
            //log the error
            console.log('error 102');
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
        input108: input108,
        input107: input107,
        
        input135: input135,
        input136: input136,

        input102: input102,
        input148: input148,
        getEvents: getEvents,

        setPreference: setPreference,

        events: events,



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
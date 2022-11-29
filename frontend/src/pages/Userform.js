import React from 'react'
import Footer from '../components/footer.js'
import './Userform.css'
import { useState } from 'react';




function Userform() {
    
    const [checked108, setChecked1] = React.useState(false);
    const [checked148, setChecked2] = React.useState(false);
    const [checked135, setChecked3] = React.useState(false);
    const [checked136, setChecked4] = React.useState(false);
    const [checked137, setChecked5] = React.useState(false);
    const [checked102, setChecked6] = React.useState(false);
    const [checked107, setChecked7] = React.useState(false);
    const [morning, setMorning ] = React.useState(false);
    const [afternoon, setAfternoon] = React.useState(false);
    const [evening, setEvening] = React.useState(false);
    const [maxTime, setMaxTime] = React.useState('')
    const [contTime, setContTime] = React.useState('')
    const [monStudy, setMonStudy] = React.useState(false)
    const [tueStudy, setTueStudy] = React.useState(false)
    const [wedStudy, setWedStudy] = React.useState(false)
    const [thurStudy, setThurStudy] = React.useState(false)
    const [friStudy, setFriStudy] = React.useState(false)
    
    const handleSubmit = () =>  {
       
        
      }

    const handleChange1 = () => {
        setChecked1(!checked108);
    };
    const handleChange2 = () => {
        setChecked2(!checked148);
    };
    const handleChange3 = () => {
        setChecked3(!checked135);
    };
    const handleChange4 = () => {
        setChecked4(!checked136);
    };
    const handleChange5 = () => {
        setChecked5(!checked137);
    };
    const handleChange6 = () => {
        setChecked6(!checked102);
    };
    const handleChange7 = () => {
        setChecked7(!checked107);
    };
    const morningChange = () => {
        setMorning(!morning)
    }
    const afternoonChange = () => {
        setAfternoon(!afternoon)
    }
    const eveningChange = () => {
        setEvening(!evening)
    }

    const maxTimeChange= event => {
        setMaxTime(event.target.value)
    }
    const contTimeChange = event => {

        setContTime(event.target.value)
    }

    const monStudyChange= ()=>{
        setMonStudy(!monStudy)
    }
    const tueStudyChange= ()=>{
        setTueStudy(!tueStudy)
    }
    const wedStudyChange= ()=>{
        setWedStudy(!wedStudy)
    }
    const thurStudyChange= ()=>{
        setThurStudy(!thurStudy)
    }
    const friStudyChange= ()=>{
        setFriStudy(!friStudy)
    }


  
    return (
    <div className='userform'>
        
        <div className='form-section'>
            <div className='form'>

            <form className='input' onSubmit={handleSubmit}>
            <label>Which Courses are you currently taking?</label>
            <label>
                <input type="checkbox" checked={checked108} onChange={handleChange1}/>
                CSC108
            </label>
            <label>
                <input type="checkbox" checked={checked148} onChange={handleChange2} />
                CSC148
            </label>
            <label>
                <input type="checkbox" checked={checked135} onChange={handleChange3} />
                MAT135
            </label>
            <label>
                <input type="checkbox" checked={checked136} onChange={handleChange4}/>
                MAT136
            </label>
            <label>
                <input type="checkbox" checked={checked137} onChange={handleChange5} />
                MAT137
            </label>
            <label>
                <input type="checkbox" checked={checked102} onChange={handleChange6}/>
                MAT102
            </label>
            <label>
                <input type="checkbox" checked={checked107} onChange={handleChange7}/>
                STA107
            </label>

            <hr></hr>

            <label>Do you prefer to study in the morning, evening or night?</label>
            
            <label>
                <input type="checkbox" checked={morning} onChange={morningChange}/>
                Morning
            </label>
            <label>
                <input type="checkbox" checked={afternoon} onChange={afternoonChange} />
                Afternoon
            </label>
            <label>
                <input type="checkbox" checked={evening} onChange={eveningChange}/>
                Evening
            </label>

            <hr></hr>

            <label>What is the maximum amount of hours do you want to study per day?</label>
            <br></br>
            <label>
                <input type="text" value={maxTime} placeholder='eg: 4' onChange={maxTimeChange} ></input>
            </label>
            
            <hr></hr>


            <label>What is the maximum amount of hours that you want to study continuously?</label>
            <br></br>
            <label>
                <input type="text" value={contTime} placeholder='eg: 3' onChange={contTimeChange} ></input>
            </label>

            <hr></hr>
            <label>What days do you not want to study?</label>
            <br></br>

            <div className='study-days'>
                <label>
                    <input type="checkbox" checked={monStudy} onChange={monStudyChange} />
                    Monday
                </label>
                <label>
                    <input type="checkbox" checked={tueStudy} onChange={tueStudyChange}/>
                    Tuesday
                </label>
                <label>
                    <input type="checkbox" checked={wedStudy} onChange={wedStudyChange} />
                    Wednesday
                </label>
                <label>
                    <input type="checkbox" checked={thurStudy} onChange={thurStudyChange}/>
                    Thursday
                </label>
                <label>
                    <input type="checkbox" checked={friStudy} onChange={friStudyChange}/>
                    Friday
                </label>

            </div>
            <br></br>
            <label>
            <input type="submit" value="Submit"/>

            </label>
           
            </form>
            

                
            </div>

        
      
      
    
        </div>
        
        <Footer></Footer>

    </div>
  )
}


export default Userform

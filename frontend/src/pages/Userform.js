import React, {useState, useEffect, useContext, useRef} from 'react'
import AuthContext from '../context/AuthContext';
import Footer from '../components/footer.js'
import './Userform.css'
import NavBar from '../components/nav-bar.js';
import { useNavigate } from 'react-router-dom';




function Userform() {

    const navigate = useNavigate();
    let {input108, input148, input135, input136, input102, input107, setPreference} = useContext(AuthContext);
    
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

    const lec108 = useRef("");
    const tut108 = useRef("");
    
    const lec148 = useRef("");
    const tut148 = useRef("");
    
    const lec102 = useRef("");
    const tut102 = useRef("");
    
    const lec135 = useRef("");
    const tut135 = useRef("");

    const lec136 = useRef("");
    const tut136 = useRef("");
    
    const lec107 = useRef("");
    const tut107 = useRef("");
    
    //let selection108 = lec108.current.value;

    

    
    const handleSubmit = (e) =>  {
        e.preventDefault();
        const lec108value = lec108.current.value;
        const tut108value = tut108.current.value;
        const lec148value = lec148.current.value;
        const tut148value = tut148.current.value;
        const lec102value = lec102.current.value;
        const tut102value = tut102.current.value;
        const lec135value = lec135.current.value;
        const tut135value = tut135.current.value;
        const lec136value = lec136.current.value;
        const tut136value = tut136.current.value;
        const lec107value = lec107.current.value;
        const tut107value = tut107.current.value;

        //the variable time pref will be 0, 1 or 2, based on whether morning, afternoon or evening is selected
        let timePref = 0;
        if (morning) {
            timePref = 0;
        }
        if (afternoon) {
            timePref = 1;
        }
        if (evening) {
            timePref = 2;
        }

        setPreference(timePref, maxTime, contTime);

        if (checked108) {
            console.log('CSC108')
            console.log('this is my value for 108', lec108value)
            console.log('this is my value for 108', tut108value)

            input108(lec108value, tut108value);
        }
        if (checked148) {
            console.log('CSC148')

            input148(lec148value, tut148value);
        }
        if (checked135) {
            console.log('MAT135')

            input135(lec135value, tut135value);
        }
        if (checked136) {
            console.log('MAT136')

            input136(lec136value, tut136value);
        }
        if (checked137) {
            console.log('MAT137')
        }
        if (checked102) {
            console.log('MAT102')

            input102(lec102value, tut102value);
        }
        if (checked107) {
            console.log('STA107')

            
            input107(lec107value, tut107value);
        }
        navigate('/');
      }

    const handleChange1 = () => {
        setChecked1(!checked108);
        console.log(lec108.current.value)
        
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
        setAfternoon(false)
        setEvening(false)
    }
    const afternoonChange = () => {
        setAfternoon(!afternoon)
        setMorning(false)
        setEvening(false)
    }
    const eveningChange = () => {
        setEvening(!evening)
        setMorning(false)
        setAfternoon(false)
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

    

    function getTimings(prefix, num){
        
        let list = []
        for (let i = 0; i < num; i++) {
            if(i<9){
                list.push(prefix.concat("010".concat((i+1).toString())))
            }else{
                list.push(prefix.concat("01".concat((i+1).toString())))
            }
            
        }
        return list
    }

 
    

    return (
        
    <div className='userform'>
        
        
        <div className='form-section'>
            <div className='form'>
            
            
            <form className='input' onSubmit={handleSubmit}>
            
            
            <label>Which Courses are you currently taking?</label>
            <label className='checkInput'>
                <input  type="checkbox" name='csc108' checked={checked108} onChange={handleChange1}/>
                CSC108
                <Dropdown id = 'lec108' reference={lec108} timings = {getTimings("LEC",7)}/>
                <Dropdown id = 'tut108' reference={tut108} timings = {getTimings("PRA",23)}/>

            </label>
            <label className='checkInput'>
                <input  type="checkbox" name='csc148' checked={checked148} onChange={handleChange2} />
                CSC148
                <Dropdown id = 'lec148' reference={lec148} timings = {getTimings("LEC",7)}/>
                <Dropdown id = 'tut148' reference={tut148} timings = {getTimings("PRA",25)}/>
            </label>
            <label className='checkInput'>
                <input  type="checkbox" name='mat135' checked={checked135} onChange={handleChange3} />
                Mat135
                <Dropdown id = 'lec135' reference={lec135} timings = {getTimings("LEC",9)}/>
                <Dropdown id = 'tut135' reference={tut135} timings = {getTimings("TUT",36)}/>
            </label >
            <label className='checkInput' >
                <input  type="checkbox" name='mat136' checked={checked136} onChange={handleChange4}/>
                Mat136
                <Dropdown id = 'lec136' reference={lec136} timings = {getTimings("LEC",2)}/>
                <Dropdown id = 'tut136' reference={tut136} timings = {getTimings("TUT",9)}/>
            </label >
            {/* <label className='checkInput'>
                <input  type="checkbox" name='mat137' checked={checked137} onChange={handleChange5} />
                Mat137
                <Dropdown id = 'lec137' timings = {getTimings("LEC",2)}/>
                <Dropdown id = 'tut137' timings = {getTimings("TUT",7)}/>
            </label> */}
            <label className='checkInput'>
                <input  type="checkbox" name='mat102' checked={checked102} onChange={handleChange6}/>
                MAT102
                <Dropdown id = 'lec102' reference={lec102} timings = {getTimings("LEC",9)}/>
            <Dropdown id = 'tut102' reference={tut102} timings = {getTimings("TUT",36)}/>
            </label>
            <label className='checkInput'>
                <input type="checkbox" name='sta107' checked={checked107} onChange={handleChange7}/>
                STA107  
                <Dropdown id = 'lec107' reference={lec107} timings = {getTimings("LEC",4)}/>
                <Dropdown id = 'tut107' reference={lec107} timings = {getTimings("TUT",16)}/>
            </label>

            <hr></hr>

            <label>Do you prefer to study in the morning, evening or night?</label>
            
            <label>
                <input type="checkbox" name='morning' checked={morning} onChange={morningChange}/>
                Morning
            </label>
            <label>
                <input type="checkbox" name='afternoon' checked={afternoon} onChange={afternoonChange} />
                Afternoon
            </label>
            <label>
                <input type="checkbox" name='evening' checked={evening} onChange={eveningChange}/>
                Evening
            </label>

            <hr></hr>

            <label>What is the maximum amount of hours do you want to study per day?</label>
            <br></br>
            <label>
                <input type="number" name='maxstudy' value={maxTime} min={1} max={12} placeholder='eg: 4' onChange={maxTimeChange} ></input>
            </label>
            
            <hr></hr>


            <label>What is the maximum amount of hours that you want to study continuously?</label>
            <br></br>
            <label>
                <input type="number" name='contstudy' value={contTime} min={1} max={4} onChange={contTimeChange}  placeholder='eg: 3'></input>
            </label>

            <hr></hr>
 
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





function Dropdown(props) {
  const [selectedOption, setSelectedOption] = useState('');

  
  return (
    <div>
      

      {/* //<label>Select a number: </label> */}
      <select ref={props.reference} value={selectedOption} onChange={e => {
        setSelectedOption(e.target.value)
           }}>
        {props.timings.map(num => (
          <option key={num} value={num}>
            {num}
          </option>
        ))}
      </select>
    </div>
  );
}


export default Userform;

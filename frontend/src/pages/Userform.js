import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext';
import Footer from '../components/footer.js'
import './Userform.css'
import NavBar from '../components/nav-bar.js';
import { useNavigate } from 'react-router-dom';




function Userform() {

    const navigate = useNavigate();
    let {input108, input148, input135, input136, input102, input107} = useContext(AuthContext);
    
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


    
    const handleSubmit = (e) =>  {
        e.preventDefault();
        if (checked108) {
            console.log('CSC108')
            input108();
        }
        if (checked148) {
            console.log('CSC148')
            input148();
        }
        if (checked135) {
            console.log('MAT135')
            input135();
        }
        if (checked136) {
            console.log('MAT136')
            input136();
        }
        if (checked137) {
            console.log('MAT137')
        }
        if (checked102) {
            console.log('MAT102')
            input102();
        }
        if (checked107) {
            console.log('STA107')
            input107();
        }
        navigate('/');
      }

    const handleChange1 = () => {
        setChecked1(!checked108);
        toggleHidden();
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


    const lectures108 = [];//7;
    const tutorials108 = [];//23;
    
    const lectures148 = [];//7 ;
    const tutorials148 = [];//25 ['PRA0101', 'PRA0102', 'PRA0102', 'PRA0102', 'PRA0105', 'LEC0106', 'LEC0107'];

    const lectures135 = ["LEC0112", "LEC0114"];//['LEC0101', 'LEC0102', 'LEC0102', 'LEC0102', 'LEC0105', 'LEC0106', 'LEC0107'];
    const tutorials135 =[];// ['LEC0101', 'LEC0102', 'LEC0102', 'LEC0102', 'LEC0105', 'LEC0106', 'LEC0107'];

    const lectures136 = [];//['LEC0101', 'LEC0102', 'LEC0102', 'LEC0102', 'LEC0105', 'LEC0106', 'LEC0107'];
    const tutorials136 =[];// ['LEC0101', 'LEC0102', 'LEC0102', 'LEC0102', 'LEC0105', 'LEC0106', 'LEC0107'];

    const lectures137 = [];//['LEC0101', 'LEC0102', 'LEC0102', 'LEC0102', 'LEC0105', 'LEC0106', 'LEC0107'];
    const tutorials137 = [];//['LEC0101', 'LEC0102', 'LEC0102', 'LEC0102', 'LEC0105', 'LEC0106', 'LEC0107'];

    const lectures102 = [];//9;
    const tutorials102 = [];//36;

    const lectures107 = [];//;
    const tutorials107 = [];//;

    

    function getTimings(prefix, num){
        
        let list = []
        for (let i = 0; i < num; i++) {
            if(i<10){
                list.push(prefix.concat("010".concat((i+1).toString())))
            }else{
                list.push(prefix.concat("01".concat((i+1).toString())))
            }
            
        }
        return list
    }

    function toggleHidden(id){
        let element = document.getElementsById("dropdown")
        let hidden = element.getAttribute("hidden")
        if(hidden){
            element.removeAttribute("hidden")
        }else{
            element.setAttribute("hidden", "hidden")
        }

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
                <Dropdown id = 'lec108' timings = {getTimings("LEC",7)}/>
                <Dropdown id = 'tut108' timings = {getTimings("PRA",23)}/>
            </label>
            <label className='checkInput'>
                <input  type="checkbox" name='csc148' checked={checked148} onChange={handleChange2} />
                CSC148
                <Dropdown id = 'lec148' timings = {getTimings("LEC",7)}/>
                <Dropdown id = 'tut148' timings = {getTimings("PRA",25)}/>
            </label>
            <label className='checkInput'>
                <input  type="checkbox" name='mat135' checked={checked135} onChange={handleChange3} />
                Mat135
                <Dropdown id = 'lec102' timings = {getTimings("LEC",9)}/>
                 <Dropdown id = 'tut102' timings = {getTimings("TUT",36)}/>
            </label >
            <label className='checkInput' >
                <input  type="checkbox" name='mat136' checked={checked136} onChange={handleChange4}/>
                Mat136
                <Dropdown id = 'lec136' timings = {getTimings("LEC",2)}/>
                <Dropdown id = 'tut136' timings = {getTimings("TUT",9)}/>
            </label >
            <label className='checkInput'>
                <input  type="checkbox" name='mat137' checked={checked137} onChange={handleChange5} />
                Mat137
                <Dropdown id = 'lec137' timings = {getTimings("LEC",2)}/>
                <Dropdown id = 'tut137' timings = {getTimings("TUT",7)}/>
            </label>
            <label className='checkInput'>
                <input  type="checkbox" name='mat102' checked={checked102} onChange={handleChange6}/>
                MAT102
                <Dropdown id = 'lec102' timings = {getTimings("LEC",9)}/>
            <Dropdown id = 'tut102' timings = {getTimings("TUT",36)}/>
            </label>
            <label className='checkInput'>
                <input type="checkbox" name='sta107' checked={checked107} onChange={handleChange7}/>
                STA107  
                <Dropdown id = 'lec107' timings = {getTimings("LEC",4)}/>
                <Dropdown id = 'tut107' value = {null} timings = {getTimings("TUT",16)}/>
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
                <input type="number" name='contstudy' value={contTime} min={1} max={4} onChange={contTimeChange} ></input>
            </label>

            <hr></hr>
            <label>What days do you not want to study?</label>
            <br></br>

            <div className='study-days'>
                <label>
                    <input type="checkbox" name='monStudy' checked={monStudy} onChange={monStudyChange} />
                    Monday
                </label>
                <label>
                    <input type="checkbox" name='tueStudy' checked={tueStudy} onChange={tueStudyChange}/>
                    Tuesday
                </label>
                <label>
                    <input type="checkbox" name='wedStudy' checked={wedStudy} onChange={wedStudyChange} />
                    Wednesday
                </label>
                <label>
                    <input type="checkbox" name='thuStudy' checked={thurStudy} onChange={thurStudyChange}/>
                    Thursday
                </label>
                <label>
                    <input type="checkbox" name='friStudy' checked={friStudy} onChange={friStudyChange}/>
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

function Dropdown(props) {
  const [selectedOption, setSelectedOption] = useState(null);

  
  return (
    <div>
      
      {/* //<label>Select a number: </label> */}
      <select value={selectedOption} onChange={e => {
        setSelectedOption(e.target.value)}}>
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

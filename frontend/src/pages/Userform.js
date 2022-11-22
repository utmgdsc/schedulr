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
                Mat135
            </label>
            <label>
                <input type="checkbox" checked={checked136} onChange={handleChange4}/>
                Mat136
            </label>
            <label>
                <input type="checkbox" checked={checked137} onChange={handleChange5} />
                Mat137
            </label>
            <label>
                <input type="checkbox" checked={checked102} onChange={handleChange6}/>
                MAT102
            </label>
            <label>
                <input type="checkbox" checked={checked107} onChange={handleChange7}/>
                MAT102
            </label>

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

const Checkbox = ({ label, value, onChange }) => {
    return (
      <label>
        <input type="checkbox" checked={value} onChange={onChange} />
        {label}
      </label>
    );
  };

export default Userform

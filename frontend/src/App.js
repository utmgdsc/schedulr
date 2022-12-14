
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage'; 
import LoginPage from './pages/LoginPage';
import Header from './components/Header';
import PrivateRoute from './utils/PrivateRoute';

import { AuthProvider } from './context/AuthContext';
import RegisterPage from './pages/RegisterPage';
import Userform from './pages/Userform';


function App() {
  return (
    <div className="App">
    <AuthProvider>
    <Header />

        <Routes>
          {/* commented for debugging */}
          <Route element= {<PrivateRoute><HomePage/></PrivateRoute>} path="/" exact/>
          <Route element= {<Userform/>} path ='/userform' />
          {/* <Route element= {<HomePage/>} path="/" exact/> */}
          <Route element={ <LoginPage />} path="/login"/>
          <Route element={ <RegisterPage />} path="/register"/>
        </Routes>
</AuthProvider>
    </div>
  );
}

export default App;

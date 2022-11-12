
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage'; 
import LoginPage from './pages/LoginPage';
import Header from './components/Header';
import PrivateRoute from './utils/PrivateRoute';

import { AuthProvider } from './context/AuthContext';


function App() {
  return (
    <div className="App">
    <AuthProvider>
    <Header />

        <Routes>
          <Route element= {<PrivateRoute><HomePage/></PrivateRoute>} path="/" exact/>
          <Route element={ <LoginPage />} path="/login"/>
        </Routes>
</AuthProvider>
    </div>
  );
}

export default App;

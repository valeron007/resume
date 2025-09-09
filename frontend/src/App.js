
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link, Navigate, useLocation } from "react-router-dom";
import LoginForm from "./components/LoginForm.js"
import GetResumes from "./components/Resumes.js"
import CreateResume from "./components/CreateResume.js"
import ResumeCard from "./components/ResumeCard.js"

export default function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>              
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>            
            <li>
              <Link to="/create">Added new resume</Link>
            </li>            
          </ul>
        </nav>

        <Routes>
          <Route path="/" 
            element={
              <RequireAuth>
                <Home />
              </RequireAuth>
            } 
          />
          <Route path="/login" element={<Login />} />          
          <Route path="/create" 
            element={
              <RequireAuth>
                <Create />
              </RequireAuth>
            } 
          />
          <Route path="/resume/:id" element={
            <RequireAuth>
              <Card />
            </RequireAuth>
            } 
            />          
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  return <div>
    <h2>Home</h2>
    <GetResumes />
  </div>;
}

function Login() {
  return <div>
    <h2>Login</h2>    
    <LoginForm />
  </div>;
}

function Create() {
  return <div>
    <h2>Login</h2>    
    <CreateResume />
    </div>;
}

function Card() {
  return <div>
    <h2>Resume</h2>    
      <ResumeCard />
    </div>;
}

function RequireAuth({ children }) {
  let location = useLocation();
  
  if (!localStorage.getItem("access_token")) {    
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}



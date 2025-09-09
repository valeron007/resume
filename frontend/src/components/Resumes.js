import { useState, useEffect } from 'react';
import { NavLink } from "react-router-dom";

export default function GetResumes() {
    const [resumes, setResume] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8080/resume/lists', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Access-Control-Allow-Origin': '*',
                'Authorization': 'Bearer ' + localStorage.getItem("access_token")
            },
        })
        .then(response => response.json())        
        .then(data => setResume(data))        
      }, [])

    return (        
        <div class='resume-data'>
            {resumes.map((resume) => (
            <>
                <div class="resume-item">
                    <div class="resume-title"><NavLink to={`/resume/${resume.id}`}>{resume.title}</NavLink></div>                    
                    <div class="resume-content">
                        {resume.content}
                    </div>                
                </div>  
            </>            
        ))}
        </div>        
    )

}


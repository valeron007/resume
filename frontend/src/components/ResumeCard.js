import React from "react";
import { useState, useEffect } from 'react';
import { useParams } from "react-router-dom";

export default function ResumeCard() {
    const params = useParams();    
    const [resume, setResume] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8080/resume/' + params.id, {
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

    const handleClick = async () => {
        let card = document.querySelector('.content-card')

        const response = await fetch('http://127.0.0.1:8080/resume/' + params.id + '/improve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Access-Control-Allow-Origin': '*',
                'Authorization': 'Bearer ' + localStorage.getItem("access_token")
            },
            body: JSON.stringify({
                "content": card.textContent
            })
        })

        const result = await response.json();        
        card.innerHTML = result
    }
    

    return (           
        <>
        <div class='resume-card'>                        
            <div class='title-card'>{resume.title}</div>
            <div class='content-card'>{resume.content}</div>
            <button onClick={handleClick}>Improve</button>
        </div>
        </>
    )
}


import { useForm } from "react-hook-form";
import { Navigate, useNavigate } from 'react-router-dom';



export default function CreateResume() {
    function handleSubmit(e) {        
        e.preventDefault();

        const form = e.target;
        const formData = new FormData(form);                
        

        fetch('http://127.0.0.1:8080/resume/create', { 
            method: form.method, 
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Access-Control-Allow-Origin': '*',
                'Authorization': 'Bearer ' + localStorage.getItem("access_token")
            },
            body: JSON.stringify(Object.fromEntries(formData.entries()))
        }).then(response => response.json())
        .then(data => {            
            window.location.href = '/'
        })
        
  }

  return (
    <form method="post" onSubmit={handleSubmit}>
        <label>
            Title input: 
            <input name="title" defaultValue="Test" />
        </label>
        <hr />
        <label>
            Write your content:
            <textarea name="content" rows={4} cols={40} />
        </label>
      
        <hr />      
        <button type="submit">Create Resume</button>
    </form>
  );
}

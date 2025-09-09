import React from "react";
import { useForm } from "react-hook-form";
import "../App.css";

export default function LoginForm() {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm();

    const onSubmit = async (data) => {        
        const url = 'http://127.0.0.1:8080/user/login'
        let response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(data)
        });

        let result = await response.json();
        localStorage.setItem('access_token', result.access_token);
        localStorage.setItem('token_type', result.token_type);
    };
    
    return (
        <>
            <h2>Login Form</h2>

            <form className="login-form" onSubmit={handleSubmit(onSubmit)}>
                <input
                    type="email"
                    {...register("email", { required: true })}
                    placeholder="Email"
                />
                {errors.email && <span style={{ color: "red" }}>*Email* is mandatory</span>}

                <input
                    type="password"
                    {...register("password", { required: true })}
                    placeholder="Password"
                />
                {errors.password && <span style={{ color: "red" }}>*Password* is mandatory</span>}

                <input type="submit" style={{ backgroundColor: "#a1eafb" }} />
            </form>
        </>
    );
}

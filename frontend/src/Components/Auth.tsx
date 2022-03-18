import React, {useEffect, useState} from "react";
import {Button, Paper, Typography} from "@mui/material";
import {appCard} from "./Styles";
import GitHubIcon from '@mui/icons-material/GitHub';
import { GithubAuthProvider, signInWithPopup, getAuth } from "firebase/auth";
import { initializeApp } from "firebase/app";
import {firebaseConfig} from "./Firebase";

/*
    Данный компонент отвечает за авторизацию.
    Интерфейс под пропы не писал, т.к. один аргумент
*/
const Auth = (props:any) => {

    //Подключение к Firebase
    const app = initializeApp(firebaseConfig);
    const provider = new GithubAuthProvider();
    const  githubAuth = () => {
        const auth = getAuth(app);
        signInWithPopup(auth,provider).then((res)=>{
            props.saveAuth(res.user.displayName);
            return
        })
    }

    const logIn = () => {
        githubAuth();
    }

    return(
        <Paper sx={appCard}>
            <Typography variant={"h6"}>Авторизация</Typography>
            <Button onClick={logIn} variant={"contained"} style={{backgroundColor:"#171515"}}> <GitHubIcon/> Вход</Button>
        </Paper>
    )
}

export default Auth;
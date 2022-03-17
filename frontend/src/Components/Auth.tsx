import React, {useState} from "react";
import {Button,Paper, Typography} from "@mui/material";
import {appCard, appContent} from "./Styles";
import GitHubIcon from '@mui/icons-material/GitHub';

/*
    Данный компонент отвечает за авторизацию.
    Интерфейс под пропы не писал, т.к. всего два аргумента
*/
const Auth = (props:any) => {

    const logIn = () => {

    }

    return(
        <Paper sx={appCard}>
            <Typography variant={"h6"}>Авторизация</Typography>
            <Button onClick={logIn} variant={"contained"} style={{backgroundColor:"#171515"}}> <GitHubIcon/> Вход</Button>
        </Paper>
    )
}

export default Auth;
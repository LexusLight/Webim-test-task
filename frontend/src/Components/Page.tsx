import React, {useEffect, useState} from "react";
import {appCard} from "./Styles";
import {Button, Paper, Typography} from "@mui/material";
import AccessibleForwardIcon from '@mui/icons-material/AccessibleForward';
import DiamondIcon from '@mui/icons-material/Diamond';

/*
    Данный компонент отвечает за получение EventSource-сообщений и отображения числа.
    Интерфейс под пропы не писал, т.к. всего три аргумента
*/
const Page = (props:any) => {

    const [number,setNumber] = useState(0)

    const logOut = () => {
        props.exitAuth();
    }
    //При загркзке устанавливаем одно соединение с потоком событий.
    useEffect(()=>{
        const sse = new EventSource("/stream")
        const handleStream = (e:any) => {
            let data = JSON.parse(e.data);
            setNumber(data.number)
        }
        sse.onmessage = e => handleStream(e)
        sse.onerror = e => sse.close()

        // fetch("/foo").then((res)=>{
        //     console.log(res);
        // })

        return () => {
            sse.close()
        }


    },[])

    return(
        <Paper sx={appCard}>
            <DiamondIcon style={{color:"#"+number,fontSize: 50}} />
            <Typography variant={"h6"}>{props.displayName} </Typography>
            <Typography variant={"h6"}>{number} </Typography>
            <Button onClick={logOut} variant={"contained"} style={{backgroundColor:"#171515"}}> <AccessibleForwardIcon/> Выход</Button>
        </Paper>
    )
}

export default Page;
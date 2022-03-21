import React, {useEffect, useState} from "react";
import Box from '@mui/material/Box';
import Page from "./Page";
import Auth from "./Auth";
import {appContent} from "./Styles";


//Головной компонент. Здесь мы храним методы для работы над state. Дополнительные модули убраны для простоты.
const App = () => {
    const [displayName, setDisplayName] = useState("")

    const saveAuth = (name: string) => {
        setDisplayName(name);
        localStorage.setItem("displayName",name)
    }
    const loadAuth = () => {
        let name = localStorage.getItem("displayName");
        if(name)
            setDisplayName(name);
    }
    const exitAuth = () => {
        localStorage.removeItem("displayName");
        setDisplayName("");
    }

    useEffect(()=>{
        loadAuth();
    }, [])

    return(
        <Box sx={appContent}>
            {(displayName.length > 0) ? <Page displayName={displayName} setDisplayName={setDisplayName} exitAuth={exitAuth}/> : <Auth saveAuth={saveAuth}/>}
        </Box>
    )
}

export default App;
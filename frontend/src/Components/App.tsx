import React, {useState} from "react";
import Box from '@mui/material/Box';
import Page from "./Page";
import Auth from "./Auth";
import {appContent} from "./Styles";

const App = () => {
    const [authFlag, setAuthFlag] = useState( false)

    return(
        <Box sx={appContent}>
            {authFlag ? <Page authFlag={authFlag} setAuthFlag={setAuthFlag}/> : <Auth/>}
        </Box>
    )
}

export default App;
import {makeStyles} from "@mui/material";

/*
Раньше в MUI была система методов и хуков Styles.
Теперь всё поменяли.
*/
const appContent = {
    display:"flex",
    justifyContent: "center",
    alignItems: "center",
    position:"absolute",
    height:"100%",
    width:"100%",
    backgroundColor: "#1a1a1a",
    }

const appCard = {
    height:200,
    width:400,
    justifyContent: "space-evenly",
    alignItems: "center",
    display:"flex",
    flexDirection: 'column'
}

export {
    appContent,
    appCard
};
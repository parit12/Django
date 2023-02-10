import React,{ Component } from "react";
import {render} from "react-dom";
import Homepage from "./homepage";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPgae from "./RoomJoinPage";
export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (<div> <Homepage/></div>);
    }
}

const appDiv = document.getElementById("app");
render(<App name="qwerty" />,appDiv)
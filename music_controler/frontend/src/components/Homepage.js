import React, {Component} from "react";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPgae from "./RoomJoinPage";
import {BrowserRouter as Router ,Routes,Route,Link,Redirect} from "react-router-dom";
export default class Homepage extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <Router>
                <Routes>
                    <Route exact path='/'>This is a homePage </Route>
                    <Route path='/join' element={<RoomJoinPgae/>}></Route>
                    <Route path='/create' element={<CreateRoomPage/>}></Route>
                </Routes>
            </Router>
        );
    }
}
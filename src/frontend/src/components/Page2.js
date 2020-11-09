import React from 'react'
import './style.css'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

function Page2(){
    return(
        <div className="page2">
            <div className="logopage2"></div>
            <div className="searchcont">
                <div className="form">
                    <form>
                        <input className="searchbox" placeholder={"search anything..."} type="text"/>
                    </form>
                </div>
                <Router>
                    <Link to="/searchresult" className="imgsearch"></Link>
                </Router>
            </div>
        </div>
    )
}

export default Page2
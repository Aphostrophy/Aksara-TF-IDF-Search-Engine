import React from 'react'
import './style.css'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

function Header(){
    return (
        <div className="navbar-aksara">
            <div className="pic"><div className="logofit"></div></div>
            <div className="search"><Link to="/search" className="button">Search</Link></div>
            <div><Link to="/about"  className="button" >About</Link></div>
        </div>
    )
}

export default Header
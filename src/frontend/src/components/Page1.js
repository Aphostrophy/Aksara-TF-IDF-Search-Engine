import React from 'react'
import './style.css'
import Uploader from './Uploader'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

function Page1(){
    return(
        <div className="Page1">
            <div className="box1">
                <div className="headupload"></div>
                <div className="uploadcont">
                    <div className="imgupload"></div>
                    <Uploader/>
                </div>
                <div className="buttoncont">
                    <div className="contuploadbutton"><Link to="/upload" className="uploadbutton">Upload</Link></div>
                    <div className="contsearchbutton"><Link to="/search" className="searchbutton">Search</Link></div>
                </div>
            </div>
            <div className="Logogif"></div>
        </div>
    )
}
export default Page1
import React, {useState} from 'react'
import './style.css'
import { Link, Redirect } from "react-router-dom";
import Axios from 'axios'

function SearchPage(){

    const [searchQuery, setSearchQuery] = useState("")

    const handleChange= (e) => {
        e.preventDefault();
        setSearchQuery(e.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        const endpoint = `${process.env.REACT_APP_URL}/search`;
        Axios.get(endpoint,{
            params: {
                query: searchQuery
            }
        }).then((result)=>{
            <Redirect to="/result" />
        }).catch((err)=>{
            alert(err);
        })
    }

    return(
        <div className="page2">
            <div className="logopage2"></div>
            <div className="searchcont">
                <div className="form">
                    <form onSubmit={(e)=>handleSubmit(e)}>
                        <label>
                            <input className="searchbox" value={searchQuery} onChange={(e)=>handleChange(e)}/>
                        </label>
                        <input className="imgsearch" type="submit" value="Submit"></input>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default SearchPage
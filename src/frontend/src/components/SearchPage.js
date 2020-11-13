import React, { useState } from 'react'
import './style.css'
import { Link, Redirect, useHistory } from "react-router-dom";

function SearchPage() {

    const [searchQuery, setSearchQuery] = useState("")
    const history = useHistory();

    const handleChange = (e) => {
        e.preventDefault();
        setSearchQuery(e.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        history.push({
            pathname: 'result',
            state: { searchQuery: searchQuery }
        })
    }

    return (
        <div className="page2">
            <div className="logopage2"></div>
            <div className="searchcont">
                <div>
                    <form className="formPageSearch" onSubmit={(e) => handleSubmit(e)}>
                        <label>
                            <input className="searchbox" placeholder="search anything..." value={searchQuery} onChange={(e) => handleChange(e)} />
                        </label>
                        <input className="imgsearch" type="submit" value="Submit"></input>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default SearchPage
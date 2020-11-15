import React, { useState, useContext } from 'react'
import './style.scss'
import { Link, Redirect, useHistory } from "react-router-dom";
import { ThemeContext } from '../context/ThemeContext';

function SearchPage() {

    const [searchQuery, setSearchQuery] = useState("");
    const history = useHistory();
    const { theme } = useContext(ThemeContext);

    const handleChange = (e) => {
        e.preventDefault();
        setSearchQuery(e.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        history.push({
            pathname: 'result',
            state: { searchQuery: searchQuery , mode: theme}
        })
    }

    return (
        <div className="page2">
            <div className="logopage2"></div>
            <div className="searchcont">
                <div>
                    <form className="formPageSearch" onSubmit={(e) => handleSubmit(e)}>
                        <label>
                            {theme === 'normal' ? <input className="searchbox" placeholder="search anything from the files..." value={searchQuery} onChange={(e) => handleChange(e)} /> : <input className="searchbox" placeholder="search anything from the web..." value={searchQuery} onChange={(e) => handleChange(e)} />}
                        </label>
                        <input className="imgsearch" type="submit" value="Submit"></input>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default SearchPage
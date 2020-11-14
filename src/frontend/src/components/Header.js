import React, {useState,useContext} from 'react'
import './style.scss'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
import { ThemeContext } from '../context/ThemeContext';
import { ToggleButton } from '@material-ui/lab';
import {Check} from '@material-ui/icons'

function Header() {
    const { theme, toggleTheme } = useContext(ThemeContext);
    const [selected, setSelected] = useState(false);
    return (
        <div className="navbar-aksara">
            <div className="pic"><div className="logofit"></div></div>
            <div className="upload"><Link to='/upload' className="button">Upload</Link></div>
            <div className="search"><Link to="/search" className="button">Search</Link></div>
            <div><Link to="/about" className="button" >About</Link></div>
            <ToggleButton
                value="check"
                selected={selected}
                onChange={() => {
                    toggleTheme(theme === 'normal' ? 'web' : 'normal');
                    setSelected(!selected);
                }}
                >
                <Check />
            </ToggleButton>
        </div>
    )
}

export default Header
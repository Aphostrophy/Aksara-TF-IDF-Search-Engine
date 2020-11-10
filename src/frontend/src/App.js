import logo from './logo.svg';
import './App.css';
import Axios from 'axios';
import React,{useEffect} from 'react';
import Header from './components/Header';
import SearchPage from './components/SearchPage';
import UploadPage from './components/UploadPage';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

function App() {

  return (
    <div>
    <Router>
      <Header />
        <Switch>
          <Route exact path='/' component={UploadPage} />
          <Route exact path='/search' component={SearchPage} />
        </Switch>
    </Router>
    </div>
  );
}

export default App;

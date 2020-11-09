import logo from './logo.svg';
import './App.css';
import Axios from 'axios';
import React,{useEffect} from 'react';
import Header from './components/Header';
import Page1 from './components/Page1';
import Page2 from './components/Page2';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {

  return (
    <div>
    <Router>
      <Header />
        <Switch>
          <Route exact path='/' component={Page1} />
          <Route exact path='/search' component={Page2} />
        </Switch>
    </Router>
    </div>
  );
}

export default App;

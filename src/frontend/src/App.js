import logo from "./logo.svg";
import "./App.scss";
import Axios from "axios";
import React, { useEffect } from "react";
import Header from "./components/Header";
import SearchPage from "./components/SearchPage";
import UploadPage from "./components/UploadPage";
import ResultPage from "./components/ResultPage";
import About from "./components/About";
import Cerita from "./components/Cerita";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import {ThemeContextProvider} from './context/ThemeContext';

function App() {
	return (
		<ThemeContextProvider>
			<div>
				<Router>
					<Header />
					<Switch>
						<Route exact path="/" component={SearchPage} />
						<Route exact path="/upload" component={UploadPage} />
						<Route exact path="/search" component={SearchPage} />
						<Route exact path="/result" component={ResultPage} />
						<Route exact path="/about" component={About} />
						<Route exact path="/cerita" component={Cerita} />
					</Switch>
				</Router>
			</div>
		</ThemeContextProvider>
	);
}

export default App;

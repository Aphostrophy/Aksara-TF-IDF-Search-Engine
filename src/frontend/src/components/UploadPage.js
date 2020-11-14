import React from "react";
import "./style.scss";
import Uploader from "./Uploader";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function Page1() {
	return (
		<div className="Page1">
			<div className="box1">
				<div className="headupload"></div>
				<div className="uploadcont">
					<div className="imgupload"></div>
					<Uploader />
				</div>
					<div className="buttoncont">
						<div className="contsearchbutton">
							<Link to="/search" className="searchbutton">
								search
							</Link>
						</div>
					</div>
			</div>
			<div className="Logogif"></div>
		</div>
	);
}
export default Page1;

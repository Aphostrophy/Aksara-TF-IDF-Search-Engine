import React, { useEffect, useState, useContext } from "react";
import Axios from "axios";
import { useHistory } from "react-router-dom";
import "./result.scss";
import Datatable from "./TableData";
import parse from "html-react-parser";
import { ThemeContext } from "../context/ThemeContext";

export default function ResultPage(props) {
	const [searchQuery, setSearchQuery] = useState(
		props.location.state.searchQuery
	);
	const history = useHistory();
	const [data, setData] = useState([]);
	const [tab, setTable] = useState([]);
	const [ranks, setRanks] = useState([]);
	const [rowlength, setRowLength] = useState(0);
	const newrow = [];
	const [listRanks, setListRanks] = useState([]);
	const [kolom, setKolom] = useState([]);
	const { theme, toggleTheme } = useContext(ThemeContext);

	useEffect(() => {
		(async () => {
			try {
				const endpoint =
					theme === "normal"
						? `${process.env.REACT_APP_URL}/search`
						: `${process.env.REACT_APP_URL}/webscrap`;
				const { data: res } = await Axios.get(endpoint, {
					params: {
						query: searchQuery,
					},
				});
				setListRanks(res.ranks);
				if (res.table) {
					let items = new Array(Object.keys(res.table[0]).length);
					for (let i = 0; i < items.length; i++) {
						items[i] = new Array(res.table.length);
					}
					for (let i = 0; i < res.ranks.length; i++) {
						newrow[i] = res.ranks[i].title;
					}
					for (let i = 0; i < res.table.length; i++) {
						let keyss = Object.keys(res.table[i]);
						for (let j = 0; j < keyss.length; j++) {
							items[j][i] = res.table[i][keyss[j]];
						}
					}
					for (let i = 0; i < Object.keys(res.table[0]).length; i++) {
						items[i][0] = Object.keys(res.table[0])[i];
					}
					setRowLength(newrow.length);
					setTable(items);
					setKolom(res.kolom);
				}
				setRanks(res.ranks);
			} catch (err) {
				console.log(err);
			}
		})();
	}, [searchQuery]);

	if (tab) {
	}
	return (
		<div className="pageResult">
			{ranks.length !== 0 ? (
				<>
					<div className="container-ranks">
						<div className="cont-imgResult">
							<div className="imgResult"></div>
						</div>
						{tab.length !== 0 ? (
							listRanks.map((entry, i) => (
								<div key={i} className="container-rank">
									<div className="urutan">
										<b> {i + 1}</b>
									</div>
									<div
										onClick={() => {
											if (props.location.state.mode === "normal") {
												history.push({
													pathname: "cerita",
													state: { fileParams: entry.title },
												});
											} else if (props.location.state.mode === "web") {
												window.open(entry.title, "_blank");
											}
										}}>
										<b>Judul</b> :{" "}
										<div className="title-hyperlink">
											{entry.title.substring(0, 60)}
										</div>
									</div>
									<div>
										<b>Jumlah Kata</b> : {entry.wordscount}
									</div>
									<div>
										<b>Similarity</b> : {entry.similarity*100} %
									</div>
									<br />
									<div>{parse(entry.header)}</div>
								</div>
							))
						) : (
							<h1>Results not found, maybe your queries are all stopwords</h1>
						)}
					</div>
					<div className="container-result">
						<Datatable data={tab} lengthrow={rowlength} columnsss={kolom} />
					</div>
				</>
			) : (
				<div className="loadingio-spinner-eclipse-9rrd0ie4sw">
					<div className="ldio-a0aql1c9bzd">
						<div></div>
					</div>
				</div>
			)}
		</div>
	);
}

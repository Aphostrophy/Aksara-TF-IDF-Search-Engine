import React, { useEffect, useState } from "react";
import Axios from "axios";
import "./result.css";
import Datatable from "./TableData";
export default function ResultPage(props) {
	const [searchQuery, setSearchQuery] = useState(
		props.location.state.searchQuery
	);
	const [queryResult, setQueryResult] = useState(null);
	const [data, setData] = useState([]);
	const [tab, setTable] = useState([]);
	const [ranks, setRanks] = useState([]);
	const [rowlength, setRowLength] = useState(0);
	const newrow = [];
	useEffect(() => {
		(async () => {
			const endpoint = `${process.env.REACT_APP_URL}/search`;
			try {
				const { data: res } = await Axios.get(endpoint, {
					params: {
						query: searchQuery,
					},
				});
				console.log(res);
				let items = new Array(Object.keys(res.table[0]).length);
				for (var i = 0; i < items.length; i++) {
					items[i] = new Array(res.table.length);
					if (i == 0) {
					}
				}
				console.log(items);
				for (var i = 0; i < res.ranks.length; i++) {
					newrow[i] = res.ranks[i].title;
				}
				for (var i = 0; i < res.table.length; i++) {
					var keyss = Object.keys(res.table[i]);
					for (var j = 0; j < keyss.length; j++) {
						items[j][i] = res.table[i][keyss[j]];
					}
				}
				for (var i = 0; i < Object.keys(res.table[0]).length; i++) {
					items[i][0] = Object.keys(res.table[0])[i];
				}
				console.log(items);
				setRowLength(newrow.length);
				setTable(items);
				setRanks(res.ranks);
			} catch (err) {
				console.log(err);
			}
		})();
	}, [searchQuery]);

	return (
		<>
			<div className="container-result">
				<Datatable data={tab} lengthrow={rowlength} />
			</div>
		</>
	);
}

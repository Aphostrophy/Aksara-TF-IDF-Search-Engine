import React from "react";
import "./table.css";
export default function Datatable({ data, lengthrow }) {
	const columnss = ["terms", "query"];
	for (var i = 0; i < lengthrow; i++) {
		columnss.push("D" + (i + 1));
	}
	const columns = data[0] && Object.keys(data[0]);
	return (
		<table id="items" cellPadding={0} cellSpacing={0}>
			<thead>
				<tr>
					{columnss.map((heading) => (
						<th>{heading}</th>
					))}
				</tr>
			</thead>
			<tbody>
				{data.map((row) => (
					<tr>
						{columns.map((column) => (
							<td>{row[column]}</td>
						))}
					</tr>
				))}
			</tbody>
		</table>
	);
}

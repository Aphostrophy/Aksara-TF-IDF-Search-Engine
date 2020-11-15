import React from "react";
import "./table.scss";
export default function Datatable({ data, lengthrow, columnsss }) {
	const columnss = ["terms", "query"];
	for (var i = 0; i < lengthrow; i++) {
		columnss.push(columnsss[0][i]);
	}
	const columns = data[0] && Object.keys(data[0]);
	return (
		<div className="table-wrapper">
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
		</div>
	);
}

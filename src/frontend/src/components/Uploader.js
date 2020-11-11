import React, { useMemo, useState, useEffect } from "react";
import { useDropzone } from "react-dropzone";
import axios from "axios";
import "./uploader.css";

const baseStyle = {
	flex: 1,
	display: "flex",
	flexDirection: "column",
	alignItems: "center",
	padding: "20px",
	borderWidth: 2,
	borderRadius: 2,
	borderColor: "#eeeeee",
	borderStyle: "dashed",
	backgroundColor: "#fafafa",
	color: "#bdbdbd",
	outline: "none",
	transition: "border .24s ease-in-out",
	height: "220px",
};

const activeStyle = {
	borderColor: "#2196f3",
};

const acceptStyle = {
	borderColor: "#00e676",
};

const rejectStyle = {
	borderColor: "#ff1744",
};

function Uploader(props) {
	const [files, setFiles] = useState([]);
	const onDrop = (files) => {
		const uploaders = files.map((file) => {
			const formData = new FormData();
			formData.append("file", file);
			formData.append("upload_preset", "pvhilzh7");
			formData.append("api_key", "1234567");
			formData.append("timestamp", Date.now() / 1000 || 0);
			console.log(formData);
			console.log("Heyyyyyyy");
			return axios
				.post("http://localhost:5000/api/upload", formData, {
					headers: { "X-Requested-With": "XMLHttpRequest" },
				})
				.then((response) => {
					const data = response.data;
					const fileURL = data.secure_url;
					console.log(data);
				});
		});
		axios.all(uploaders).then(() => {
			console.log("success CUYYYYYYYYYYYYYYY");
		});
	};
	const {
		getRootProps,
		getInputProps,
		open,
		isDragActive,
		isDragAccept,
		isDragReject,
	} = useDropzone({
		accept: "text/html",
		noClick: true,
		noKeyboard: true,
		onDrop,
	});

	const style = useMemo(
		() => ({
			...baseStyle,
			...(isDragActive ? activeStyle : {}),
			...(isDragAccept ? acceptStyle : {}),
			...(isDragReject ? rejectStyle : {}),
		}),
		[isDragActive, isDragReject, isDragAccept]
	);

	useEffect(
		() => () => {
			files.forEach((file) => URL.revokeObjectURL(file.preview));
		},
		[files]
	);
	return (
		<>
			<div className="container">
				<div {...getRootProps({ style })}>
					<input {...getInputProps()} />
					<p>Drag 'n' drop some files here, or click to select files</p>
					<button type="button" onClick={open}>
						Click here
					</button>
				</div>
			</div>
			<button type="button">Submit</button>
		</>
	);
}

export default Uploader;

import React from "react";
import Dropzone from "react-dropzone-uploader";
import "react-dropzone-uploader/dist/styles.css";
import "./uploader.css";

const Uploader = () => {
	const getUploadParams = ({ meta }) => {
		return { url: "http://localhost:5000/api/upload" };
	};

	const handleChangeStatus = ({ meta, file }, status) => {
		console.log("CHANGEEEEEEEEEEEEEEEEEEEEEEEE");
		console.log(status, meta, file);
	};

	const handleSubmit = (files, allFiles) => {
		console.log("SUBMITTTTTTTTTTTTTTTTTT");
		console.log(files);
		console.log(files.map((f) => f.meta));
		allFiles.forEach((f) => f.remove());
	};

	return (
		<Dropzone
			getUploadParams={getUploadParams}
			onChangeStatus={handleChangeStatus}
			onSubmit={handleSubmit}
			styles={{
				dropzone: { minHeight: 300, maxHeight: 250 },
				submitButton: {
					width: 100,
					backgroundColor: "#e6e2cb",
					color: "black",
				},
				inputLabel: {
					color: "black",
				},
				inputLabelWithFiles: {
					backgroundColor: "#e6e2cb",
					color: "black",
				},
			}}
			accept=".html"
			inputContent="Drag Files or Click to Upload"
		/>
	);
};

export default Uploader;

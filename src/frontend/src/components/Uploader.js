import Axios from "axios";
import React from "react";
import Dropzone from "react-dropzone-uploader";
import "react-dropzone-uploader/dist/styles.css";
import "./uploader.css";

const Uploader = () => {

  // receives array of all files that are done uploading
  const handleSubmit = (files) => {
		const endpoint = "http://localhost:5000/api/upload"
	  console.log(files.map(f => f.meta)) 
		files.forEach(element => {
			Axios.post(endpoint,{
				file: element.meta
			})
			console.log(element.file)
		});
	}
  
  // called every time a file's `status` changes
  const handleChangeStatus = ({ meta, file }, status) => { console.log(status, meta, file) }

	return (
		<>
			<Dropzone
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
		</>
	);
};

export default Uploader;

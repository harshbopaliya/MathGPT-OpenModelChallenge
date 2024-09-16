import React, { useState } from "react";
import axios from "axios";

const MainSection = () => {
  const [file, setFile] = useState(null);
  const [problem, setProblem] = useState("");
  const [solution, setSolution] = useState("");
  const [response, setResponse] = useState("");
  const [modelFilename, setModelFilename] = useState("");

  // Handle file upload
  const handleFileUpload = (e) => {
    setFile(e.target.files[0]);
  };

  // Submit the model for upload
  const handleFileSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("model", file);

    try {
      const res = await axios.post("http://localhost:5000/api/upload-model", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setResponse(res.data.message);
      setModelFilename(res.data.model_filename); // Save the model filename
    } catch (error) {
      console.error("Error uploading model:", error);
    }
  };

  // Submit the problem for evaluation
  const handleEvaluate = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://localhost:5000/api/evaluate", {
        problem,
        solution: solution.split(',').map(Number), // Assuming solution is a comma-separated list
        model_filename: modelFilename,
      });
      setResponse(res.data.message); // Display the accuracy or other relevant message
    } catch (error) {
      console.error("Error evaluating model:", error);
    }
  };

  return (
    <main className="main-section">
      <div className="input-box">
        <form onSubmit={handleFileSubmit}>
          <h2>Upload Your Model (pkl or joblib)</h2>
          <input type="file" onChange={handleFileUpload} className="input-file" />
          <button type="submit" className="submit-button">
            Upload Model
          </button>
        </form>

        <form onSubmit={handleEvaluate}>
          <h2>Evaluate Your Model</h2>
          <input
            type="text"
            placeholder="Enter your problem"
            value={problem}
            onChange={(e) => setProblem(e.target.value)}
            className="input-field"
          />
          <input
            type="text"
            placeholder="Enter expected solution (comma-separated)"
            value={solution}
            onChange={(e) => setSolution(e.target.value)}
            className="input-field"
          />
          <button type="submit" className="submit-button">
            Evaluate Model
          </button>
        </form>

        {response && (
          <div className="response-box">
            <h3>Response from Backend:</h3>
            <p>{response}</p>
          </div>
        )}
      </div>
    </main>
  );
};

export default MainSection;

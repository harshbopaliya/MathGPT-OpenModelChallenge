import React, { useState } from "react";
import axios from "axios";

const MainSection = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://localhost:5000/api/message", {
        message,
      });
      setResponse(res.data.message);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <main className="main-section">
      <div className="input-box">
        <form onSubmit={handleSubmit}>
          <h2>Send Message to Backend</h2>
          <input
            type="text"
            placeholder="Enter your message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            className="input-field"
          />
          <button type="submit" className="submit-button">
            Send
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

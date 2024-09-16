import React from "react";
import "../styles/Header.css"; // Optional: if you have specific styles for the header

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <h1>MathGPT</h1>
        <nav>
          <ul>
            <li>
              <a href="#home">Home</a>
            </li>
            <li>
              <a href="#features">Features</a>
            </li>
            <li>
              <a href="#about">About</a>
            </li>
            <li>
              <a href="#contact">Contact</a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;

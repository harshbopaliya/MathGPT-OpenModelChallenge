import React from "react";
import "../styles/Footer.css"; // Optional: if you have specific styles for the footer

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <p>&copy; {new Date().getFullYear()} MathGPT. All rights reserved.</p>
        <nav>
          <ul>
            <li>
              <a href="#privacy">Privacy Policy</a>
            </li>
            <li>
              <a href="#terms">Terms of Service</a>
            </li>
          </ul>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;

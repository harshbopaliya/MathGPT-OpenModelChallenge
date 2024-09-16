import React from "react";
import Header from "./components/Header"; // Adjust the path if needed
import Footer from "./components/Footer"; // Adjust the path if needed

import "./styles/App.css"; // Make sure you import the CSS file
import MainSection from "./components/MainSection";

const App = () => {
  return (
    <div>
      <Header />
      <MainSection />
      <Footer />
    </div>
  );
};

export default App;

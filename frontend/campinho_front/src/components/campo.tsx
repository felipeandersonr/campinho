import React from "react";
import "./campo.css";

const Campo = () => {
  return (
    <div className="field">
        <div className="center-line"></div>

      <div className="center-circle">
        <div className="center-dot"></div>
      </div>
      <div className="goal-area top"></div>
      <div className="penalty-area top"></div>
      <div className="goal-area bottom"></div>
      <div className="penalty-area bottom"></div>
    </div>
  );
};

export default Campo;

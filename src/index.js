import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import Router from "./Router";
import ThemeProvider from "./ThemeProvider";
import "antd/dist/antd.css";
import axios from "axios";

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider>
      <Router />
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

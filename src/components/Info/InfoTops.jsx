import React, { useState, useEffect } from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import axios from "axios";

const InfoTops = () => {
  const [Date, setDate] = useState();
  const [Price, setPrice] = useState();
  const [Cap, setCap] = useState();

  async function GetInfoTops(code) {
    const response = await axios.get(
      "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/topstock/"
    );
    if (response.data) {
      console.log("투자정보", response.data);
      setDate(response.data.date);
      setPrice(response.data.price);
      setCap(response.data.cap);
    }
  }
  useEffect(() => {
    GetInfoTops();
  }, []);

  return <div>infoTops</div>;
};

export default InfoTops;

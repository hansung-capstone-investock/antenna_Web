import styled from "styled-components";
import React, { useState, useEffect, useHistory } from "react";
import axios from "axios";

async function StockSearch(code) {
  const response = await axios.post(
    "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/stocksearch/",
    { companyCode: code }
  );
  if (response.data) {
    console.log("stocksearchdata", response.data);
  }
}
const StockInfo = (query) => {
  const code = query.code;
  StockSearch(code);
};

export default StockInfo;

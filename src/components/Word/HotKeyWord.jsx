import React, { useState, useEffect } from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";

import axios from "axios";

const Wrapper = styled.div`
  width: 280px;
  height: 235px;
  border: 6px black solid;
  padding-left: 10px;
  padding-right: 10px;

  @media screen and (max-width: 1300px) {
    display: inline-block;
    margin: 0 0 0 30px;
    width: 416px;
  }
`;

const InterestList = () => {
  return <Wrapper>관심종목</Wrapper>;
};

export default InterestList;

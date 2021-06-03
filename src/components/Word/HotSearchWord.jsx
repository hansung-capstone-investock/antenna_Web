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
  margin-bottom: 30px;
  @media screen and (max-width: 1300px) {
    display: inline-block;
    margin: 0 0 0 0;
    width: 416px;
  }
`;

const HotSearchWord = () => {
  return <Wrapper>search</Wrapper>;
};

export default HotSearchWord;

import React from "react";
import styled from "styled-components";

const Box = styled.div`
  position: absolute;
  top: 400px;
  left: 67%;
  margin: 0 5%;
  display: inline;
  height: 180px;
  width: 260px;
  padding: 10px;
  box-shadow: 5px 5px 5px 5px gray;

  @media screen and (max-width: 1100px) {
    position: inherit;
    display: block;
    height: 600px;
    width: 100%;
    margin: 0px;
  }
  @media screen and (max-height: 600px) {
    position: inherit;
    display: block;
    height: 600px;
    width: 100%;
    margin: 0px;
  }
`;

const InvestBox = () => {
  return <Box>모의투자</Box>;
};

export default InvestBox;

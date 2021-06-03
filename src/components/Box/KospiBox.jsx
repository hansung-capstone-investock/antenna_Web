import React from "react";
import styled from "styled-components";
import { ChartKospi } from "../../components";

const Box = styled.div`
  position: absolute;
  top: 180px;
  left: 40%;
  margin: 0 5%;
  display: inline-block;
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

const KospiBox = () => {
  return (
    <Box>
      <p>코스피</p>
      <ChartKospi></ChartKospi>
    </Box>
  );
};

export default KospiBox;

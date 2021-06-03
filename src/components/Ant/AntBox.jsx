import React from "react";
import styled from "styled-components";
import { FirstBox, SecondBox, ThirdBox } from "../../components";
import { MText } from "../../components";

const AntBox = () => {
  const Wrapper = styled.div`
    height: 380px;
    width: 100%;
    display: inline-block;
    align-items: center;
    vertical-align: top;

    @media screen and (max-width: 1300px) {
      display: block;
      width: 100vw;
      height: calc(100vh-80px);
      margin: 0 0 0 0;
    }
  `;

  const Box = styled.div`
    background-color: ${(props) => props.color || "#e9e9e9"};
    width: 260px;
    height: 340px;
    display: inline-block;
    align-items: center;
    vertical-align: ${(props) => props.valign || "top"};
    margin: 2vw;
    padding: 10px;

    @media screen and (max-width: 1300px) {
      display: block;
      width: 100vw;
      height: 600px;
      margin: 0 0 0 0;
    }
  `;

  return (
    <Wrapper>
      <Box>
        <FirstBox></FirstBox>
      </Box>
      <Box color="#e6e6e6">
        <SecondBox></SecondBox>
      </Box>
      <Box color="#dadada" valign="middle">
        <ThirdBox></ThirdBox>
      </Box>
    </Wrapper>
  );
};

export default AntBox;

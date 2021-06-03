import React from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import { MainText } from "../../components";
import { MText } from "../../components";
import { AntBox, FirstBox, SecondBox } from "../../components";

const Wrapper = styled.div`
  margin-left: 10px;
  width: 75%;
  height: 560px;
  display: inline-block;
  vertical-align: middle;

  @media screen and (max-width: 1300px) {
    position: inherit;
    display: block;
    width: 100%;
    margin: 0 0 0 0;
  }
`;

const BoxWrapper = styled.div`
  height: 140px;
  width: 100%;
  display: inline-block;
  align-items: center;
`;

const TextWrapper = styled.div`
  width: 100%;
  margin: 0 0 10px 10px;
  vertical-align: middle;
  display: inline-block;

  @media screen and (max-width: 1300px) {
    display: block;
    width: 100vw;
    height: 600px;
    margin: 0 0 0 10px;
  }
`;

const Ant = () => {
  return (
    <Wrapper>
      <TextWrapper>
        <MainText display="inline-block">Antenna</MainText>
        <MText align="bottom" size="20px">
          와 함께하세요
        </MText>
      </TextWrapper>
      <AntBox></AntBox>
      <MText
        size="20px"
        color="black"
        float="right"
        mright="60px"
        mediaDisplay="none"
      >
        주식 초보를 위한 안테나! 사이트 곳곳의 Antenna를 찾아보세요!
      </MText>
    </Wrapper>
  );
};

export default Ant;

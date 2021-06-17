import React from "react";
import { Word } from "../../containers";
import styled from "styled-components";
import { Ant, HotSearchWord } from "../../components";

const Wrapper = styled.div`
  vertical-align: middle;
  align-items: center;
  display: inline-block;
  width: 100%;
  height: 100%;
  background-color: white;
  padding-left: 60px;
  padding-top: 20px;
`;
const Wrapper2 = styled.div`
  display: -ms-inline-grid;
  width: 360px;
  display: inline-block;
  vertical-align: middle;
  padding-left: 30px;
  position: absolute;

  @media screen and (max-width: 1300px) {
    display: none;
  }
`;
const Antenna = (props) => {
  return (
    <Wrapper>
      <Ant></Ant>
    </Wrapper>
  );
};

export default Antenna;

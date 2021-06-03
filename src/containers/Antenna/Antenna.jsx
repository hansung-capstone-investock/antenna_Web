import React from "react";
import { Word } from "../../containers";
import styled from "styled-components";
import { Ant, HotKeyWord, HotSearchWord } from "../../components";

const Wrapper = styled.div`
  vertical-align: middle;
  margin-top: 20px;
  align-items: center;
  display: inline-block;
`;
const Wrapper2 = styled.div`
  display: -ms-inline-grid;
  width: 360px;
  display: inline-block;
  vertical-align: middle;
  margin-left: 10px;
  position: absolute;
  right: 0px;

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

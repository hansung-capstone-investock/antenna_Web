import React from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import { HotKeyWord, HotSearchWord } from "../../components";

const Wrapper = styled.div`
  display: -ms-inline-grid;
  width: 360px;
  display: inline-block;
  vertical-align: middle;
  margin-left: 10px;
  position: absolute;
  right: 5px;

  @media screen and (max-width: 1300px) {
    position: inherit;
    display: ${(props) => props.display || "flex"};
    justify-content: space-between;
    margin-left: 30px;
    height: 600px;
    width: 90%;
  }
`;

const Word = (props) => {
  return (
    <Wrapper>
      <HotSearchWord></HotSearchWord>
      <HotKeyWord></HotKeyWord>
    </Wrapper>
  );
};

export default Word;

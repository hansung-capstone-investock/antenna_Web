import React from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import { ItemBox, HotSearchWord } from "../../components";

const Wrapper = styled.div`
  display: -ms-inline-grid;
  height: 100%;
  width: 360px;
  vertical-align: middle;

  @media screen and (max-width: 1300px) {
    display: none;
  }
`;
const WordWrapper = styled.div`
  width: 80%;
  height: 490px;
  border: 5px solid #30475e;
  background-color: white;
  margin-top: ${(props) => props.mtop || "0"};
`;

const Word = (props) => {
  return (
    <Wrapper>
      <WordWrapper>
        <HotSearchWord />
      </WordWrapper>
    </Wrapper>
  );
};

export default Word;

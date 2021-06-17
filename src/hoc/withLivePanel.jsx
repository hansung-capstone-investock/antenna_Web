import React, { useEffect, useRef } from "react";
import { Word } from "../containers";
import styled from "styled-components";

const Wrapper = styled.div`
  width: 100%;
  min-height: 100%;
  display: inline-flex;
  padding: 10px;
  background-color: ${(props) => (props.color ? "white" : "#f05454")};
  @media screen and (max-width: 1300px) {
    flex-direction: column;
    min-height: 0px;
  }
`;

const PageContentsWrap = styled.div`
  flex: 1;
`;

const WordWrap = styled.div`
  margin-top: 20px;
  margin-right: 10px;
  @media screen and (max-width: 1300px) {
    ${(props) => props.smallDelete && "display: none"};
  }
`;

const withLivePanel = (Comp, smallDelete) => (props) => {
  return (
    <Wrapper color={smallDelete}>
      <PageContentsWrap>
        <Comp {...props} wordComp></Comp>
      </PageContentsWrap>
      <WordWrap smallDelete={smallDelete}>
        <Word></Word>
      </WordWrap>
    </Wrapper>
  );
};

export default withLivePanel;

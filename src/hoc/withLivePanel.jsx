import React, { useEffect, useRef } from "react";
import { Word } from "../containers";
import styled from "styled-components";

const Wrapper = styled.div`
  width: 100%;
  min-height: 100%;
  display: flex;
  @media screen and (max-width: 1300px) {
    flex-direction: column;
    min-height: 0px;
  }
`;

const PageContentsWrap = styled.div`
  flex: 1;
`;

const WordWrap = styled.div`
  padding-top: 20px;
  @media screen and (max-width: 1300px) {
    ${(props) => props.smallDelete && "display: none"};
  }
`;

const withLivePanel = (Comp, smallDelete) => (props) => {
  return (
    <Wrapper>
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

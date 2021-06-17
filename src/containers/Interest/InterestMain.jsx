import React, { useState } from "react";
import styled from "styled-components";
import InterestList from "../../components/Interest/InterestList";

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  background-color: #e4e4e4;
`;

const InterestMain = () => {
  return (
    <Wrapper>
      <InterestList />
    </Wrapper>
  );
};
export default InterestMain;

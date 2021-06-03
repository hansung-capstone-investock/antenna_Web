import React from "react";
import styled from "styled-components";
import { MText } from "../../components";

const FirstBox = () => {
  const Wrapper = styled.div`
    width: 200px;
    height: 100px;
  `;
  return (
    <Wrapper>
      <MText color="blue">3달</MText>
      <MText color="black">전에 알았더라면?</MText>
    </Wrapper>
  );
};

export default FirstBox;

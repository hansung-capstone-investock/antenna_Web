import React from "react";
import styled from "styled-components";
import { MText } from "../../components";

const SecondBox = () => {
  const Wrapper = styled.div`
    width: 200px;
    height: 100px;
  `;
  return (
    <Wrapper>
      <MText color="black">커피 한잔으로</MText>
      <br />
      <MText color="black">주식 시작해보기</MText>
    </Wrapper>
  );
};

export default SecondBox;

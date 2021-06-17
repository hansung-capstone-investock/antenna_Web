import React, { useState } from "react";
import styled from "styled-components";
import { MainText, MText } from "../../components";

/**
 * 관심종목을 등록하세요!
 */

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  .animated {
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
  }
  .animated.infinite {
    -webkit-animation-iteration-count: infinite;
    animation-iteration-count: infinite;
  }
  .animated.hinge {
    -webkit-animation-duration: 2s;
    animation-duration: 2s;
  }
  /*the animation definition*/
  @-webkit-keyframes fadeInDown {
    0% {
      opacity: 0;
      -webkit-transform: translate3d(0, -100%, 0);
      transform: translate3d(0, -100%, 0);
    }
    100% {
      opacity: 1;
      -webkit-transform: none;
      transform: none;
    }
  }
  @keyframes fadeInDown {
    0% {
      opacity: 0;
      -webkit-transform: translate3d(0, -100%, 0);
      -ms-transform: translate3d(0, -100%, 0);
      transform: translate3d(0, -100%, 0);
    }
    100% {
      opacity: 1;
      -webkit-transform: none;
      -ms-transform: none;
      transform: none;
    }
  }
  .fadeInDown {
    -webkit-animation-name: fadeInDown;
    animation-name: fadeInDown;
  }
`;

const TextAni = styled(MText)`
  transition: 2;
`;

const DoIntBox = () => {
  return (
    <Wrapper>
      <MText
        className="fadeInDown animated"
        font="a고딕15"
        size="30px"
        display="inline-flex"
        padBot="0"
        color="#30475e"
      >
        관심 종목
        <MText
          font="a고딕13"
          size="30px"
          display="inline-flex"
          color="#30475e"
          padBot="0"
        >
          을
        </MText>
      </MText>
      <MText
        font="a고딕13"
        size="30px"
        color="#30475e"
        className="fadeInDown animated"
      >
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;확인하세요
      </MText>
    </Wrapper>
  );
};

export default DoIntBox;

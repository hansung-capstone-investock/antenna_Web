import { RightOutlined } from "@ant-design/icons";
import React from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import { MainText } from "../../components";
import { MText } from "../../components";

const GoAntTest = () => {
  const Wrapper = styled.div`
    width: 100%;
    height: 100%;
  `;

  const IconWrapper = styled.div`
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
    @-webkit-keyframes pulse {
      0% {
        -webkit-transform: scale3d(1, 1, 1);
        transform: scale3d(1, 1, 1);
      }
      50% {
        -webkit-transform: scale3d(1.05, 1.05, 1.05);
        transform: scale3d(1.05, 1.05, 1.05);
      }
      100% {
        -webkit-transform: scale3d(1, 1, 1);
        transform: scale3d(1, 1, 1);
      }
    }
    @keyframes pulse {
      0% {
        -webkit-transform: scale3d(1, 1, 1);
        -ms-transform: scale3d(1, 1, 1);
        transform: scale3d(1, 1, 1);
      }
      50% {
        -webkit-transform: scale3d(1.05, 1.05, 1.05);
        -ms-transform: scale3d(1.05, 1.05, 1.05);
        transform: scale3d(1.05, 1.05, 1.05);
      }
      100% {
        -webkit-transform: scale3d(1, 1, 1);
        -ms-transform: scale3d(1, 1, 1);
        transform: scale3d(1, 1, 1);
      }
    }
    .pulse {
      -webkit-animation-name: pulse;
      animation-name: pulse;
    }
  `;

  return (
    <Wrapper>
      <IconWrapper>
        <MText className="pulse animated" size="70px">
          >
        </MText>
      </IconWrapper>
    </Wrapper>
  );
};

export default GoAntTest;

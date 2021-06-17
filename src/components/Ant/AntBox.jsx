import React from "react";
import styled from "styled-components";
import { FirstBox, SecondBox, ThirdBox } from "../../components";
import { MText } from "../../components";
import { Link } from "react-router-dom";

const AntBox = () => {
  const Wrapper = styled.div`
    height: 380px;
    width: 100%;
    display: inline-block;
    align-items: center;
    vertical-align: top;
    /*base code*/
    .animated {
      -webkit-animation-duration: 2s;
      animation-duration: 2s;
      -webkit-animation-fill-mode: both;
      animation-fill-mode: both;
    }
    .animated.infinite {
      -webkit-animation-iteration-count: infinite;
      animation-iteration-count: infinite;
    }
    .animated.hinge {
      -webkit-animation-duration: 3s;
      animation-duration: 3s;
    }
    /*the animation definition*/
    @-webkit-keyframes fadeIn {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 1;
      }
    }
    @keyframes fadeIn {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 1;
      }
    }
    .fadeIn {
      -webkit-animation-name: fadeIn;
      animation-name: fadeIn;
    }
  `;

  const Box = styled.div`
    width: 100%;
    height: 500px;
    display: inline-block;
    align-items: center;
    padding: 140px 10px 10px 40px;
  `;
  const AntLink = styled(Link)`
    text-decoration: none;
    color: #f14b4b;
    padding: 7px;
    background-color: #dddddd75;
  `;
  const text = "<< 백테스팅으로 전략 분석 <<";
  return (
    <Wrapper>
      <Box>
        <MText
          className="fadeInDown animated"
          font="a고딕15"
          size="30px"
          display="inline-flex"
          padBot="0"
          color="#f14b4b"
        >
          안테나
          <MText
            font="a고딕13"
            size="28px"
            display="inline-flex"
            color="#222831"
            padBot="0"
          >
            와 함께하는
          </MText>
        </MText>
        <MText
          font="a고딕13"
          size="28px"
          color="#222831"
          className="fadeInDown animated"
        >
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;당신의 투자 전략
        </MText>
        <MText
          className="fadeInDown animated"
          font="a고딕15"
          size="28px"
          display="inline-flex"
          padBot="0"
          color="#30475E"
        >
          <AntLink to="/main/backtest" className="fadeIn animated">
            {text}
          </AntLink>
        </MText>
      </Box>
    </Wrapper>
  );
};

export default AntBox;

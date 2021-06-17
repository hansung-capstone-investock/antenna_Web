import React from "react";
import styled from "styled-components";
import { FirstBox, ThirdBox } from "../../components";
import { MText } from "../../components";
import Typewriter from "typewriter-effect";
import { Link } from "react-router-dom";

const SecondBox = () => {
  const Wrapper = styled.div`
    height: 380px;
    width: 100%;
    display: inline-block;
    align-items: center;
    vertical-align: top;
  `;

  const Box = styled.div`
    width: 100%;
    height: 500px;
    display: block;
    align-items: center;
    padding: 180px 10px 10px 30px;

    /*base code*/
    .animated {
      -webkit-animation-duration: 3s;
      animation-duration: 3s;
      -webkit-animation-fill-mode: both;
      animation-fill-mode: both;
    }
    .animated.infinite {
      -webkit-animation-iteration-count: infinite;
      animation-iteration-count: infinite;
    }
    .animated.hinge {
      -webkit-animation-duration: 8s;
      animation-duration: 8s;
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

  const AntLink = styled(Link)`
    text-decoration: none;
    font-size: 28px;
    color: #f14b4b;
    padding: 9px;
    background-color: #dddddd75;
  `;
  const Twrapper = styled.div`
    width: 100%;
  `;
  return (
    <Wrapper>
      <Box>
        <MText
          className="fadeInDown animated"
          font="a고딕13"
          size="30px"
          display="inline-block"
          padBot="0"
          color="#30475E"
        >
          <Twrapper>
            <Typewriter
              onInit={(typewriter) => {
                typewriter
                  .pauseFor(500)
                  .typeString("이제는 놓치지 마세요")
                  .start();
              }}
            ></Typewriter>
          </Twrapper>
          <AntLink to="/main/antenna/test" className="fadeIn animated">
            &nbsp;>> 예측하러 가기 >>&nbsp;
          </AntLink>
        </MText>
      </Box>
    </Wrapper>
  );
};

export default SecondBox;

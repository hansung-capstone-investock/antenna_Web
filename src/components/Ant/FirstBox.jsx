import styled from "styled-components";
import { MText } from "../../components";
import axios from "axios";
import React, { useState, useEffect, useCallback } from "react";
import { List, Typography, Divider } from "antd";

const FirstBox = () => {
  const Wrapper = styled.div`
    width: 300px;
    height: 500px;
    padding: 70px 10px 0px 30px;

    .ant-list-bordered {
      border: 0;
    }
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
    @-webkit-keyframes fadeInLeft {
      0% {
        opacity: 0;
        -webkit-transform: translate3d(-100%, 0, 0);
        transform: translate3d(-100%, 0, 0);
      }
      100% {
        opacity: 1;
        -webkit-transform: none;
        transform: none;
      }
    }
    @keyframes fadeInLeft {
      0% {
        opacity: 0;
        -webkit-transform: translate3d(-100%, 0, 0);
        -ms-transform: translate3d(-100%, 0, 0);
        transform: translate3d(-100%, 0, 0);
      }
      100% {
        opacity: 1;
        -webkit-transform: none;
        -ms-transform: none;
        transform: none;
      }
    }
    .fadeInLeft {
      -webkit-animation-name: fadeInLeft;
      animation-name: fadeInLeft;
    }
  `;

  const Box = styled.div`
    width: 100%;
    height: 500px;
    display: inline-block;
    align-items: center;
  `;

  const [ThreeList, setThreeList] = useState([]);
  const [view, setView] = useState();
  useEffect(() => {
    const fetchThreeList = async () => {
      try {
        setThreeList(null);

        const response = await axios.get(
          "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/compare3/",
          (req, res) => {
            req.header("Access-Control-Allow-Origin", "*");
            res.header("Access-Control-Allow-Origin", "*");
          }
        );
        setThreeList(response.data); // 데이터는 response.data 안에 들어있습니다.
        console.log("Three", response.data);
      } catch (e) {}
    };

    fetchThreeList();
  }, []);
  const data = [];

  useEffect(() => {
    if (ThreeList) {
      ThreeList.map((th, key) => {
        if (th.rank < 6) {
          data.push(th);
        }
      });
    }
  }, [ThreeList]);

  return (
    <Wrapper>
      <List
        className="fadeInLeft animated"
        size="small"
        header={
          <div>
            <MText color="black" font="a고딕15" size="20px">
              3달
            </MText>
            <MText color="black" font="a고딕13" size="18px">
              전에 알았더라면?
            </MText>
          </div>
        }
        bordered
        dataSource={data}
        renderItem={(item, idx) => (
          <List.Item>
            <MText color="#1b287b">{idx + 1}</MText>
            &nbsp; &nbsp;
            <MText color="#4f4f4f" font="a고딕11">
              {item.company}
            </MText>
            &nbsp; &nbsp; &nbsp; &nbsp;
            <MText color="red" font="a아시아헤드1" float="right">
              &nbsp; ▲&nbsp;{item.gap}&nbsp;%
            </MText>
          </List.Item>
        )}
      />
    </Wrapper>
  );
};

export default FirstBox;

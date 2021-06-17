import { Tabs } from "antd";
import styled from "styled-components";
import React, { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";
import { SwapRightOutlined } from "@ant-design/icons";
import { ChartKosdaq } from "../../components";
import { MainText } from "../../components";
import { MText } from "../../components";
import NewsData from "../News/NewsData";
import LiveNews from "../News/LiveNews";

const { TabPane } = Tabs;
const Wrapper = styled.div`
  width: 80%;
  height: 80%;
  background-color: white;
  .ant-tabs-nav {
    margin-bottom: 0px;
  }
`;
const NewsWrapper = styled.div`
  width: 100%;
  height: 220px;
  //뉴스리스트 size를 margin bottom으로
  margin-bottom: 80px;
`;

//페이지 이동 링크 텍스트
const GotoPage = styled(Link)`
  text-decoration: none;
  font-family: "nanumRoundB";
  font-weight: 600;
  color: #f14b4b;
  font-size: 16px;
`;
function callback(key) {
  console.log(key);
}
const NewsforMain = () => {
  const logged = window.sessionStorage.getItem("logged");

  return (
    <Wrapper>
      <Tabs defaultActiveKey="1" type="line" onChange={callback}>
        <TabPane
          tab={
            <MText display="inline-flex" alitem="flex-start" padBot="0px">
              주요뉴스
            </MText>
          }
          key="1"
        >
          <NewsWrapper>
            <NewsData />
          </NewsWrapper>
        </TabPane>
        <TabPane
          tab={
            <MText display="inline-flex" alitem="flex-start" padBot="0px">
              실시간뉴스
            </MText>
          }
          key="2"
        >
          <NewsWrapper>
            <LiveNews />
          </NewsWrapper>
        </TabPane>
        <TabPane
          tab={
            <MText display="inline-flex" alitem="flex-start" padBot="0px">
              관심뉴스
            </MText>
          }
          key="3"
        >
          <NewsWrapper>
            {logged === "true" ? (
              <GotoPage
                to="/main/interest"
                font="nanumRoundB"
                color="#f14b4b"
                alitem="flex-start"
                padBot="0px"
              >
                관심종목 설정하고 뉴스 골라 보기
                <SwapRightOutlined />
              </GotoPage>
            ) : (
              <div>로그인하셈</div>
            )}
          </NewsWrapper>
        </TabPane>
      </Tabs>
    </Wrapper>
  );
};

export default NewsforMain;

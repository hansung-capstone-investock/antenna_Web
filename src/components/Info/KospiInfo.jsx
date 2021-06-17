import { Tabs } from "antd";
import styled from "styled-components";
import React, { useEffect, useState } from "react";
import { SwapRightOutlined } from "@ant-design/icons";
import { ChartKospi, ChartKospi200 } from "../../components";
import { Link, useHistory } from "react-router-dom";
import { ChartKosdaq } from "../../components";
import { MainText } from "../../components";
import { MText } from "../../components";
//import "./KospiInfo.css";

const { TabPane } = Tabs;

const Wrapper = styled.div`
  width: 80%;
  height: 80%;
  background-color: white;
  .ant-tabs-nav {
    margin-bottom: 8px;
  }
  div.ant-tabs-nav > div.ant-tabs-nav-wrap {
    padding-left: 30px;
  }
  .ant-tabs-ink-bar .ant-tabs-ink-bar-animated {
    background-color: black;
  }
`;
const ChartWrapper = styled.div`
  width: ${(props) => props.chartW || "450px"};
  height: ${(props) => props.chartH || "200px"};

  //오늘의 증시 보러가기 텍스트 때문에 margin
  margin-bottom: 60px;
`;
var colors = ["red", "red", "red"];

//Kospi Tab 코스피 탭
var todayKospi = window.localStorage.getItem("todayKospi");
var KospiDiffint = todayKospi - window.localStorage.getItem("lastKospi");
var KospiText = String(todayKospi);
var KospiDiff = "";

if (KospiDiffint < 0) {
  colors[0] = "blue";
  KospiDiff = "  ▼ " + String(KospiDiffint).substr(0, 6);
} else {
  colors[0] = "red";
  KospiDiff = "  ▲" + String(KospiDiffint).substr(0, 6);
}
console.log("kospidiff", KospiDiffint);
console.log("kospitext", KospiText);

//Kosdaq Tab 코스닥 탭
var todayKosdaq = window.localStorage.getItem("todayKosdaq");
var KosdaqDiffint = todayKosdaq - window.localStorage.getItem("lastKosdaq");
var KosdaqText = String(todayKosdaq);
var KosdaqDiff = "";

if (KosdaqDiffint < 0) {
  colors[1] = "blue";
  KosdaqDiff = "  ▼ " + String(KosdaqDiffint).substr(0, 6);
} else {
  colors[1] = "Red";
  KosdaqDiff = "  ▲" + String(KosdaqDiffint).substr(0, 6);
}

//Kospi 200 Tab 코스피 200 탭
var today200Kospi = window.localStorage.getItem("today200Kospi");
var last200Kospi = window.localStorage.getItem("last200Kospi");
var Kospi200Diffint = today200Kospi - last200Kospi;
var Kospi200Text = String(today200Kospi);
var Kospi200Diff = "";

if (Kospi200Diffint < 0) {
  colors[2] = "blue";
  Kospi200Diff = "  ▼ " + String(Kospi200Diffint).substr(0, 6);
} else {
  colors[2] = "red";
  Kospi200Diff = "  ▲" + String(Kospi200Diffint).substr(0, 6);
}

//페이지 이동 링크 텍스트
const GotoPage = styled(Link)`
  text-decoration: none;
  font-family: "nanumRoundB";
  font-weight: 600;
  color: #f14b4b;
  font-size: 16px;
`;
const KospiInfo = (text) => {
  console.log("text?", text);
  const [abledKey, setAbledKey] = useState("1");
  const [textColor, setTextColor] = useState(colors);

  function callback(key) {
    console.log(key);
    setAbledKey(key);
  }

  return (
    <Wrapper>
      <Tabs defaultActiveKey="1" type="line" onChange={callback}>
        <TabPane
          tab={
            <MText display="inline-flex" alitem="flex-start" padBot="0px">
              &nbsp;코스피&nbsp;&nbsp;
              {abledKey == "1" ? (
                <MText display="inline-flex" color={textColor[0]}>
                  {KospiText}
                  <MText color={textColor[0]} size="12px" alitem="flex-start">
                    {KospiDiff}
                  </MText>
                </MText>
              ) : (
                ""
              )}
            </MText>
          }
          key="1"
        >
          <ChartWrapper chartH={text.chartH} chartW={text.chartW}>
            <ChartKospi></ChartKospi>
          </ChartWrapper>
          {text.text == true ? (
            <GotoPage to="/main/infoThresh">
              오늘의 증시 보러가기 <SwapRightOutlined />
            </GotoPage>
          ) : (
            <div></div>
          )}
        </TabPane>
        <TabPane
          tab={
            <MText display="inline-flex" alitem="flex-start" padBot="0px">
              &nbsp;코스닥&nbsp;&nbsp;
              {abledKey == "2" ? (
                <MText display="inline-flex" color={textColor[1]}>
                  {KosdaqText}
                  <MText color={textColor[1]} size="12px" alitem="flex-start">
                    {KosdaqDiff}
                  </MText>
                </MText>
              ) : (
                ""
              )}
            </MText>
          }
          key="2"
        >
          <ChartWrapper chartH={text.chartH} chartW={text.chartW}>
            <ChartKosdaq></ChartKosdaq>
          </ChartWrapper>
          {text.text == true ? (
            <GotoPage to="/main/infoThresh">
              오늘의 증시 보러가기 <SwapRightOutlined />
            </GotoPage>
          ) : (
            <div></div>
          )}
        </TabPane>
        <TabPane
          tab={
            <MText display="inline-flex" alitem="flex-start" padBot="0px">
              &nbsp;코스피 200&nbsp;&nbsp;
              {abledKey == "3" ? (
                <MText
                  display="inline-flex"
                  color={textColor[2]}
                  alitem="flex-start"
                >
                  {Kospi200Text}
                  <MText color={textColor[2]} size="12px" alitem="flex-start">
                    {Kospi200Diff}
                  </MText>
                </MText>
              ) : (
                ""
              )}
            </MText>
          }
          key="3"
        >
          <ChartWrapper chartH={text.chartH} chartW={text.chartW}>
            <ChartKospi200></ChartKospi200>
          </ChartWrapper>
          {text.text == true ? (
            <GotoPage to="/main/infoThresh">
              오늘의 증시 보러가기 <SwapRightOutlined />
            </GotoPage>
          ) : (
            <div></div>
          )}
        </TabPane>
      </Tabs>
    </Wrapper>
  );
};

export default KospiInfo;

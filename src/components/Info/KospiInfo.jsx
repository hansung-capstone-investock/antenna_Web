import { Tabs } from "antd";
import styled from "styled-components";
import React, { useEffect } from "react";
import { ChartKospi } from "../../components";

const { TabPane } = Tabs;

function callback(key) {
  console.log(key);
}

const Wrapper = styled.div`
  width: 400px;
  height: 600px;
`;

const KospiInfo = () => {
  return (
    <Tabs defaultActiveKey="1" onChange={callback}>
      <TabPane tab="1일" key="1">
        1일
        <Wrapper>
          <ChartKospi></ChartKospi>
        </Wrapper>
      </TabPane>
      <TabPane tab="3개월" key="2">
        3개월
      </TabPane>
      <TabPane tab="1년" key="3">
        1년
      </TabPane>
    </Tabs>
  );
};

export default KospiInfo;

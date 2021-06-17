import React, { useState, useEffect } from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import axios from "axios";
import { Tabs } from "antd";
import { MText } from "../../components";
import { Table, Tag, Space } from "antd";

const { TabPane } = Tabs;

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
`;

const InfoTops = () => {
  const [Data, setData] = useState();
  const [Date, setDate] = useState();
  const [Price, setPrice] = useState();
  const [PriceTabel, setPriceTable] = useState();
  const [Cap, setCap] = useState();
  const [CapTable, setCapTable] = useState();

  async function GetInfoTops(code) {
    const response = await axios.get(
      "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/topstock/"
    );
    if (response.data) {
      console.log("투자정보", response.data);
      setDate(response.data.date);
      setPrice(response.data.price);
      setCap(response.data.cap);
      setData(response.data);
    }
  }
  useEffect(() => {
    GetInfoTops();
  }, []);

  const table = (data) => {
    const arr = [];
    data.map((top, idx) => {});

    const col = [];
    return (
      <Table
        className="table-striped-rows"
        dataSource={arr}
        columns={arr}
        scroll={{ x: 0, y: 500 }}
        pagination={false}
      />
    );
  };
  useEffect(() => {
    table(Price);
  }, [Data]);

  const OnChange = (props) => {
    console.log("onchange", props);
  };

  return (
    <Wrapper>
      <MText font="a아시아헤드2" size="20px" color="red">
        Top
        <MText color="black" padding="3px 0 0 0">
          &nbsp;종목
        </MText>
      </MText>
      <Tabs
        onChange={OnChange}
        type="card"
        animated={{ inkBar: true, tabPane: false }}
      >
        <TabPane tab="상한가" key="1">
          Content of Tab Pane 1
        </TabPane>
        <TabPane tab="거래량 상위" key="2">
          Content of Tab Pane 2
        </TabPane>
      </Tabs>
    </Wrapper>
  );
};

export default InfoTops;

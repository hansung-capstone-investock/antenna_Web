import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { Link, useHistory } from "react-router-dom";
import ReactDOM from "react-dom";
import axios from "axios";
import { Tabs } from "antd";
import { MText } from "../../components";
import { Table, Tag, Space } from "antd";
import {
  MinusCircleOutlined,
  LineOutlined,
  PlusCircleOutlined,
} from "@ant-design/icons";

const { TabPane } = Tabs;

const Wrapper = styled.div`
  width: 100%;
  height: 350px;
  padding: 10px 15px;
  border: 2px solid #dddddd;

  div.ant-table-header > table > thead > tr > th {
    background-color: white;
    font-family: "a고딕13";
    color: #808080;
  }
`;

const InfoTops = () => {
  const [Data, setData] = useState();
  const [Date, setDate] = useState();
  const [Price, setPrice] = useState();
  const [PriceTable, setPriceTable] = useState();
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

  //관심종목 관련 데이터
  const [Int, setInt] = useState([]);

  const table = (data) => {
    const MyLink = styled(Link)`
      text-decoration: none;
      color: black;
    `;
    //관심종목 추가 버튼 클릭 시
    const AddInt = (props) => {
      axios
        .post(
          "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/account/api/intereststockWeb/",
          {
            name: window.sessionStorage.getItem("id"),
          }
        )
        .catch(function (error) {
          console.log(error);
        })
        .then((response) => {
          if (response) {
            console.log("관심종목==> ", response.data);
            const Ints = response.data;
          }
        });
      console.log("props", props);
    };

    const FindCode = (text) => {
      var Code = "";
      console.log("Text?", text);
      Price.map((p, idx) => {
        if (p.company == text) {
          Code = p.stockcode;
        }
      });
      Cap.map((c, idx) => {
        if (c.company == text) {
          Code = c.stockcode;
        }
      });
      if (!Code) {
        Code = "error";
      }
      return Code;
    };

    if (data) {
      data.map((d, idx) => {
        if (String(d.diff).split(".").length > 1) {
          var before = String(d.diff).split(".");
          d.diff = before[0] + "." + before[1].substring(0, 2);
        }
      });
    }
    const col = [
      {
        title: "순위",
        dataIndex: "rank",
        width: "10%",
        render: (text) =>
          text == 1 ? (
            <MText font="a고딕15" size="15px" color="#0ca22a">
              &nbsp;{text}&nbsp;
            </MText>
          ) : (
            <MText font="a고딕15" size="13px" color="black">
              &nbsp;{text}&nbsp;
            </MText>
          ),
      },
      {
        title: "종목명",
        dataIndex: "company",
        width: "30%",
        render: (text, i) => (
          <MText font="a고딕11" size="12px">
            <MyLink
              to={`/main/infoThresh/stock?code=${FindCode(text)}&name=${text}`}
            >
              {text}
            </MyLink>
          </MText>
        ),
      },
      {
        title: "현재가",
        dataIndex: "todayPrice",
        render: (text) => (
          <MText font="a고딕13" size="11px">
            {text}
          </MText>
        ),
      },
      {
        title: "전일비",
        dataIndex: "diff",
        render: (text) =>
          text < 0 ? (
            <MText font="a고딕13" size="11px" color="blue">
              ▼&nbsp;{text}&nbsp;%
            </MText>
          ) : (
            <MText font="a고딕13" size="11px" color="red">
              ▲&nbsp;{text}&nbsp;%
            </MText>
          ),
      },
      {
        title: "",
        dataIndex: "company",
        width: "5%",
        render: (text) => (
          <MText font="a고딕13" size="13px" color="#098021" padding="2px 0 0 0">
            <PlusCircleOutlined onClick={() => AddInt(text)} />
          </MText>
        ),
      },
    ];
    return (
      <Table
        className="table-striped-rows"
        dataSource={data}
        columns={col}
        scroll={{ x: 0, y: 500 }}
        pagination={false}
      />
    );
  };
  useEffect(() => {
    setPriceTable(table(Price));
    setCapTable(table(Cap));
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
          {PriceTable}
        </TabPane>
        <TabPane tab="거래량 상위" key="2">
          {CapTable}
        </TabPane>
      </Tabs>
    </Wrapper>
  );
};

export default InfoTops;

import { ChartKospi, KospiInfo, KospiData, MText } from "../../components";
import styled from "styled-components";
import React, { useState, useEffect, useHistory } from "react";
import queryString from "query-string";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  ReferenceLine,
} from "recharts";
import { Table, Tag, Space } from "antd";
import { Row, Col } from "antd";
/**
 * 투자정보 기업 상세 페이지
 * @returns
 */
const InfoThreshStock = () => {
  const Wrapper = styled.div`
    height: 100%;
    width: 100%;
    padding: 20px;
    display: inline-flex;

    .ant-table-wrapper {
      height: 400px;
    }
    .ant-table-cell {
      padding: 4px;
      height: 17px;
    }
  `;
  const BoxWrapper = styled.div`
    height: 80%;
    width: 50%;
  `;
  const [query, setQuery] = useState(
    queryString.parse(document.location.search)
  );
  useState(() => {
    if (Object.keys(query).length) {
      //query가 있으면 투자정보 검색한것
      console.log("query?", query);
      StockSearch(query.code);
    } else {
      console.log("no query");
    }
  }, []);
  const defaultView = () => {
    return <div></div>;
  };

  const [StockData, setStockData] = useState();
  const [NewsData, setNewsData] = useState();
  const [view, setView] = useState(defaultView);
  //query있을 때 axios=> 차트랑 뷰 셋팅해줌
  async function StockSearch(code) {
    console.log("code???", code);
    const response = await axios.post(
      "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/stocksearch/",
      { companyCode: code }
    );
    if (response.data) {
      console.log("stocksearchdata", response.data);
      const arr = [];
      const starr = response.data.stockData;
      starr.map((st, key) => {
        arr.push({ date: st.date, close: st.close });
      });
      setStockData(response.data.stockData);
      setNewsData(response.data.newsData);
      setChartData(arr);
      setView(table(response.data));
    }
  }

  //차트 그리는 함수
  const [ChartData, setChartData] = useState([]);

  //전일대비 계산
  const [Diff, setDiff] = useState([]);
  //테이블 그리는 함수
  const table = (data) => {
    const arr = [];
    const starr = data.stockData;
    const difarr = [];
    starr.map((st, key) => {
      if (key < 1) {
        difarr.push(0);
      } else {
        var diff = st.close - starr[key - 1].close;
        difarr.push(diff);
      }
    });
    starr.map((st, key) => {
      if (key == 0) {
        const diff = st.close - starr[1].close;
        const diffrate = Math.floor((diff / st.close) * 100);
        console.log("diff!!!!!!!1", diff, diffrate);
        setDiff({ diff: diff, diffrate: diffrate });
      }
      arr.push({
        key: `${key}`,
        날짜: st.date,
        종가: st.close,
        전일대비: difarr[key],
        시가: st.open,
        고가: st.high,
        저가: st.low,
      });
    });
    const col = [
      {
        title: "날짜",
        dataIndex: "날짜",
        render: (text) => (
          <MText font="a고딕11" size="11px" color="#5a5a5a">
            {text}
          </MText>
        ),
      },
      {
        title: "종가",
        dataIndex: "종가",
        render: (text) => (
          <MText font="a고딕11" size="11px">
            {text}
          </MText>
        ),
      },
      {
        title: "전일대비",
        dataIndex: "전일대비",
        render: (text) =>
          text < 0 ? (
            <MText font="a고딕11" size="11px" color="blue">
              ▼&nbsp;{text}
            </MText>
          ) : (
            <MText font="a고딕11" size="11px" color="red">
              ▲&nbsp;{text}
            </MText>
          ),
      },
      {
        title: "시가",
        dataIndex: "시가",
        render: (text) => (
          <MText font="a고딕11" size="11px">
            {text}
          </MText>
        ),
      },
      {
        title: "고가",
        dataIndex: "고가",
        render: (text) => (
          <MText font="a고딕11" size="11px">
            {text}
          </MText>
        ),
      },
      {
        title: "저가",
        dataIndex: "저가",
        render: (text) => (
          <MText font="a고딕11" size="11px">
            {text}
          </MText>
        ),
      },
    ];

    return (
      <Table
        className="table-striped-rows"
        dataSource={arr}
        columns={col}
        scroll={{ x: 0, y: 500 }}
        pagination={false}
      />
    );
  };
  const [Close, setClose] = useState();
  const [Volume, setVolume] = useState();
  useEffect(() => {
    if (StockData) {
      setClose(StockData[0].close);
      setVolume(StockData[0].volume);
    }
  }, [StockData]);
  return (
    <Wrapper>
      <BoxWrapper>
        <Row>
          <Col span={12}>
            <MText
              font="a아시아헤드1"
              size="30px"
              color="#000000"
              padding="0 0 0 10px"
            >
              {query.name}
            </MText>
          </Col>
          <Col span={12}>
            {Diff.diff < 0 ? (
              <MText
                font="a고딕13"
                size="25px"
                color="blue"
                padding="4px 0 0 0 "
              >
                ▼&nbsp;&nbsp;{Close}
              </MText>
            ) : (
              <MText
                font="a고딕13"
                size="25px"
                color="red"
                padding="4px 0 0 0 "
              >
                ▲&nbsp;&nbsp;{Close}
              </MText>
            )}
          </Col>
        </Row>
        <Row>
          <Col span={12}>
            {" "}
            <MText
              font="a아시아헤드1"
              size="14px"
              color="#585858"
              display="inline-flex"
              padding="0 0 0 10px"
            >
              거래량&nbsp;&nbsp;{Volume}
            </MText>
          </Col>
          <Col span={12}>
            {" "}
            <MText
              font="a아시아헤드1"
              size="14px"
              color="#585858"
              display="inline-flex"
            >
              전일대비&nbsp;&nbsp;
              {Diff.diff < 0 ? (
                <MText
                  font="a아시아헤드1"
                  size="14px"
                  color="blue"
                  display="inline-flex"
                  padding="0 0 0 0"
                >
                  ▼&nbsp;{Diff.diff},&nbsp;&nbsp;{Diff.diffrate}%
                </MText>
              ) : (
                <MText
                  font="a아시아헤드1"
                  size="14px"
                  color="red"
                  display="inline-flex"
                  padding="0 0 0 0"
                >
                  ▲&nbsp;{Diff.diff},&nbsp;&nbsp;{Diff.diffrate}%
                </MText>
              )}
            </MText>
          </Col>
        </Row>
        <br />
        <br />
        <ResponsiveContainer width="90%" height="70%">
          <LineChart
            width={100}
            height={100}
            data={ChartData}
            margin={{
              top: 5,
              right: 10,
              left: 0,
              bottom: 0,
            }}
          >
            <XAxis dataKey="date" tick={{ fontSize: 10 }} reversed={true} />
            <YAxis
              dataKey="close"
              type="number"
              domain={["auto", "auto"]}
              tick={{ fontSize: 10 }}
            />
            <Tooltip formatter={(val) => [val, "종가"]} />
            <Line
              type="monotone"
              dataKey="close"
              stroke="#ff0000"
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>
        <Row>
          <Col span={24}></Col>
        </Row>
      </BoxWrapper>
      <BoxWrapper>{view}</BoxWrapper>
    </Wrapper>
  );
};
export default InfoThreshStock;

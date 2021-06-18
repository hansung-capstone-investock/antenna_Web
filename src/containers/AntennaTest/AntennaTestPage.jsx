import styled from "styled-components";
import React, { useState, useEffect } from "react";
import { LoadingOutlined } from "@ant-design/icons";
import { AntennaChart, MainText, MText } from "../../components";
import TextField from "@material-ui/core/TextField";
import Autocomplete from "@material-ui/lab/Autocomplete";
import axios from "axios";
import {
  message,
  Input,
  Button,
  Select,
  Space,
  Collapse,
  Checkbox,
  Row,
  Col,
} from "antd";
import { Spin, Alert } from "antd";

import { AntennaSubmit } from "../../components";
import { ResponsiveLine } from "nivo";
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

import indicatorList from "./indicatorList";
import stocklist from "./stocklist.json";

const CheckboxGroup = Checkbox.Group;
const { Panel } = Collapse;
const { Option } = Select;

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  display: inline-flex;
  padding: ${(props) => props.padding || "30px"};
  background-color: #30475e;

  .collapse .collapse-panel {
    margin-bottom: 24px;
    overflow: hidden;
    background: #f05454;
    border: 0px;
    border-radius: 2px;
  }
  .ant-btn {
    background: white;
    color: #f05454;
    font-weight: 700;
    font-family: "nanumRoundL";
    border: white;
  }

  .ant-collapse > .ant-collapse-item > .ant-collapse-header {
    color: white;
    font-family: "nanumRoundB";
  }
`;

const ButtonWrapper = styled.div`
  width: 100%;
  text-align: center;
  margin: 10px;
`;
const BoxWrapper = styled.div`
  width: ${(props) => props.w || "55%"};
  height: 100%;
  display: inline-block;
  padding: ${(props) => props.padding || "0"};
`;

const AntennaTestPage = () => {
  /**
   * 보조지표 체크박스
   * @param {*} e
   */
  //기본 보조지표 체크 함수
  const [company, setCompany] = useState({});
  const [checkedIndicator, setCheckedIndicator] = useState([]);
  const [diff, setDiff] = useState(true);
  const [diffrate, setDiffrate] = useState(true);
  const [date, setDate] = useState(7);
  const onChangeDefaultIdc = (e) => {
    var Idc = e.target.value;
    if (Idc == "diff") {
      if (e.target.checked) {
        setDiff(true);
      } else {
        setDiff(false);
      }
    } else {
      if (e.target.checked) {
        setDiffrate(true);
      } else {
        setDiffrate(false);
      }
    }
  };

  //추가 보조지표 체크 함수
  const onChangeIndicator = (list) => {
    setCheckedIndicator(list);
    console.log("checkedlist", list);
  };

  /**
   * 예측일
   */
  const onChangeDate = (value) => {
    console.log(value, "일");
    setDate(value);
  };

  /**
   * 제출 시 경고
   */
  const warning = (value) => {
    message.warning(value, 1);
  };
  /**
   * 제출 submit
   */

  const submit = () => {
    const checkedlist = [];
    checkedIndicator.map((check) => {
      checkedlist.push(check);
    });
    if (diff) {
      checkedlist.push("diff");
    }
    if (diffrate) {
      checkedlist.push("diffrate");
    }
    console.log("checkedlist!!!!!", checkedlist);
    if (!company.code) {
      warning("주식을 선택하세요.");
      return;
    }
    if (checkedlist.length < 2) {
      warning("보조지표는 최소 2개를 선택해야합니다.");
      return;
    }
    const data = {
      companyCode: company.code,
      predictDate: date,
      indicator: checkedlist,
    };

    AntennaSubmit(data);
    const SpinDiv = styled.div`
      width: 100%;
      margin: 200px 0 0 300px;
    `;
    setView(
      <SpinDiv>
        <Spin tip="예측중입니다..."></Spin>
      </SpinDiv>
    );
  };

  async function AntennaSubmit(data) {
    const response = await axios.post(
      "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/tensor/antenna/",
      data
    );
    console.log("Antenna", response.data);
    console.log("나온다...", response.data.actual);

    AntennaChart(response.data);
  }

  const [AntData, setAntData] = useState({});

  const [actData, setActData] = useState([]);
  const [preData, setPreData] = useState([]);

  const [chartArr, setChartArr] = useState([]);
  const [YLine, setYLine] = useState();
  const AntennaChart = (data) => {
    console.log(data);
    const preArr = [];
    const predict = data.predict;

    setPreData(preArr);

    const actArr = [];
    const act = data.actual;
    const chArr = [];
    let i = 1;
    for (var key in predict) {
      if (act[key]) {
        chArr.push({ x: "", 예측치: predict[key], 실제: act[key] });
        console.log("if act", act[key]);
      } else {
        chArr.push({ x: i + "일", 예측치: predict[key], 실제: null });
        console.log("else act", act[key]);
        setYLine(i);
        i++;
      }
    }
    setAntData(data);
    setActData(actArr);
    setChartArr(chArr);
  };

  const Box = styled.div`
    width: 700px;
    height: 300px;
    margin-left: 60%;
    display: block;
  `;

  const [view, setView] = useState(
    <Box>
      <MText
        padding="100px 0 0 100px"
        className="fadeInDown animated"
        font="a고딕15"
        size="30px"
        display="inline-flex"
        padBot="0"
        color="#f05454"
      >
        주가예측
      </MText>
      <br />
      <MText
        padding="0 0 0 100px"
        font="a고딕13"
        size="30px"
        color="#DDDDDD"
        className="fadeInDown animated"
      >
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;조건을 입력하여
        예측하기
      </MText>
    </Box>
  );
  useEffect(() => {
    console.log("chartArr", chartArr);
    const GreenLine = chartArr.length - date - 1;
    if (chartArr.length > 0) {
      setView(
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            width={600}
            height={300}
            data={chartArr}
            margin={{
              top: 5,
              right: 10,
              left: 0,
              bottom: 0,
            }}
          >
            <YAxis
              dataKey="실제"
              type="number"
              domain={["dataMin - 1500", "dataMax + 5000"]}
              tick={{ fontSize: 10 }}
              stroke="#a9a9a9"
            />
            <ReferenceLine x={GreenLine} stroke="green" />
            <XAxis dataKey="x" stroke="#a9a9a9" />
            <Line
              type="monotone"
              dataKey="실제"
              stroke="#a9a9a9"
              dot={false}
              connectNulls
            />
            <Tooltip />
            <Line
              type="monotone"
              dataKey="예측치"
              stroke="#ffa011"
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>
      );
    } else
      setView(
        <viewBox>
          <MText
            className="fadeInDown animated"
            padding="100px 0 0 100px"
            font="a고딕15"
            size="30px"
            display="inline-flex"
            padBot="0"
            color="#f05454"
          >
            주가 예측
          </MText>
          <br />
          <MText
            padding="0 0 0 100px"
            font="a고딕13"
            size="30px"
            color="#DDDDDD"
            className="fadeInDown animated"
          >
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;조건을
            입력하여 예측하기
          </MText>
        </viewBox>
      );
  }, [chartArr]);
  return (
    <Wrapper>
      <BoxWrapper w="45%">
        <Collapse className="collapse" defaultActiveKey={["1", "2", "3"]}>
          <Panel header="주식" key="1" className="collapse-panel">
            <Autocomplete
              id="searchStock"
              company={company}
              onChange={(e, newcompany) => {
                if (newcompany) {
                  setCompany({
                    code: newcompany.code,
                    company: newcompany.company,
                  });
                } else {
                  setCompany({});
                }
                console.log("val", company);
              }}
              options={stocklist}
              getOptionLabel={(option) => option.company}
              style={{ width: 300 }}
              renderInput={(params) => (
                <TextField {...params} label="종목명" variant="outlined" />
              )}
            ></Autocomplete>
          </Panel>
          <Panel header="보조지표" key="2" className="collapse-panel">
            <Row>
              <Checkbox
                value="diff"
                defaultChecked={true}
                onChange={onChangeDefaultIdc}
              >
                전일비
              </Checkbox>
              <Checkbox
                value="diffrate"
                defaultChecked={true}
                onChange={onChangeDefaultIdc}
              >
                등락률
              </Checkbox>
              <CheckboxGroup
                options={indicatorList}
                value={checkedIndicator}
                onChange={onChangeIndicator}
              ></CheckboxGroup>
            </Row>
          </Panel>
          <Panel header="예측일" key="3" className="collapse-panel">
            <Select
              defaultValue={7}
              style={{ width: 120 }}
              onChange={onChangeDate}
            >
              <Option value={7}>7일</Option>
              <Option value={14}>14일</Option>
              <Option value={21}>21일</Option>
              <Option value={28}>28일</Option>
            </Select>
          </Panel>
        </Collapse>
        <ButtonWrapper className="btn">
          <Button type="primary" className="SubmitBtn" onClick={submit}>
            테스트하기
          </Button>
        </ButtonWrapper>
      </BoxWrapper>

      <BoxWrapper padding="0 20px 30px 20px">{view}</BoxWrapper>
    </Wrapper>
  );
};

export default AntennaTestPage;

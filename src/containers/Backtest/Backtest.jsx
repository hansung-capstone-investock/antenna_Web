import styled from "styled-components";
import {
  Form,
  Input,
  Button,
  DatePicker,
  Space,
  Collapse,
  Checkbox,
  Divider,
  Slider,
  Row,
  Col,
  InputNumber,
} from "antd";
import { Spin, Alert } from "antd";
import { MainText, MText } from "../../components";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ReferenceLine } from "recharts";
import {
  ConsoleSqlOutlined,
  MinusCircleOutlined,
  PlusOutlined,
  ArrowDownOutlined,
} from "@ant-design/icons";
import axios from "axios";
import moment from "moment";
import React, { useState, useEffect } from "react";
import "./Backtest.css";
import sectorKospi from "./sectorKospi.json";
import sectorKosdaq from "./sectorKosdaq.json";
import BacktestChart from "./BacktestChart";
import { useHistory } from "react-router";

const Wrapper = styled.div`
  width: 100%;
  display: inline-flex;
  height: 200vh;
  background-color: #30475e;
  padding: ${(props) => props.padding || "30px"};
`;

const BoxWrapper = styled.div`
  width: ${(props) => props.w || "50%"};
  height: 100%;
  display: inline-block;
  padding: ${(props) => props.padding || "0"};
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
  @-webkit-keyframes fadeInDown {
    0% {
      opacity: 0;
      -webkit-transform: translate3d(0, -100%, 0);
      transform: translate3d(0, -100%, 0);
    }
    100% {
      opacity: 1;
      -webkit-transform: none;
      transform: none;
    }
  }
  @keyframes fadeInDown {
    0% {
      opacity: 0;
      -webkit-transform: translate3d(0, -100%, 0);
      -ms-transform: translate3d(0, -100%, 0);
      transform: translate3d(0, -100%, 0);
    }
    100% {
      opacity: 1;
      -webkit-transform: none;
      -ms-transform: none;
      transform: none;
    }
  }
  .fadeInDown {
    -webkit-animation-name: fadeInDown;
    animation-name: fadeInDown;
  }
`;
const ConditionWrapper = styled.div`
  width: 100%;
  align-items: center;
  vertical-align: middle;

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
const { Panel } = Collapse;
const { RangePicker } = DatePicker;
const CheckboxGroup = Checkbox.Group;
const Backtest = () => {
  const [start, setstart] = useState();
  const [end, setend] = useState();

  const user = window.sessionStorage.getItem("id");
  const sectorPanel = "시장구분";

  /**
   * 체크박스 Checkbox
   * 업종(Sector) 가져와서 저장
   */
  //코스피 업종
  const KospiSectorCode = Object.keys(sectorKospi);
  const KospiSectorName = Object.values(sectorKospi);
  const KospiSector = [];
  KospiSectorCode.map((code, idx) => {
    KospiSector.push({ label: KospiSectorName[idx], value: code });
  });
  const [kospiCode, setKospiCode] = useState();
  const [checkedListKospi, setCheckedListKospi] = useState();
  const [indeterminateKospi, setIndeterminateKospi] = useState();
  const [checkAllKospi, setCheckAllKospi] = useState();
  const onChangeKospi = (list) => {
    console.log("kospilist", list);
    setCheckedListKospi(list);
    if (list) {
      setKospiCode("1");
    } else {
      setKospiCode("");
    }
    setIndeterminateKospi(
      !!list.length && list.length < KospiSectorCode.length
    );
    setCheckAllKospi(list.length === KospiSectorCode.length);
  };
  const onCheckAllChangeKospi = (e) => {
    setCheckedListKospi(e.target.checked ? KospiSectorCode : []);
    if (e.target.checked) {
      setKospiCode("1");
    } else {
      setKospiCode("");
    }
    setIndeterminateKospi(false);
    setCheckAllKospi(e.target.checked);
  };

  //코스닥 업종
  const KosdaqSectorCode = Object.keys(sectorKosdaq);
  const KosdaqSectorName = Object.values(sectorKosdaq);
  const KosdaqSector = [];
  KosdaqSectorCode.map((code, idx) => {
    KosdaqSector.push({ label: KosdaqSectorName[idx], value: code });
  });
  const [kosdaqCode, setKosdaqCode] = useState();
  const [checkedListKosdaq, setCheckedListKosdaq] = useState();
  const [indeterminateKosdaq, setIndeterminateKosdaq] = useState();
  const [checkAllKosdaq, setCheckAllKosdaq] = useState();
  const onChangeKosdaq = (list) => {
    setCheckedListKosdaq(list);
    if (list) {
      setKosdaqCode("2");
    } else {
      setKosdaqCode("");
    }
    setIndeterminateKosdaq(
      !!list.length && list.length < KosdaqSectorCode.length
    );
    setCheckAllKosdaq(list.length === KosdaqSectorCode.length);
  };
  const onCheckAllChangeKosdaq = (e) => {
    setCheckedListKosdaq(e.target.checked ? KosdaqSectorCode : []);
    console.log("checked?", e.target.checked);
    if (e.target.checked) {
      setKosdaqCode("2");
    } else {
      setKosdaqCode("");
    }
    setIndeterminateKosdaq(false);
    setCheckAllKosdaq(e.target.checked);
  };

  /**
   *  RangePicker : Date, 시작일/종료일
   * */
  //달력 diable 날짜 셋팅
  function disabledDate(current) {
    return (
      (current && current < moment("2008-01-01", "YYYY-MM-DD")) ||
      current >= moment().subtract(1, "days")
    );
  }

  //달력 날짜 값
  const updateDate = (dates, dateStrings) => {
    console.log("updateDate", dateStrings[0], dateStrings[1]);
    setstart(dateStrings[0]);
    setend(dateStrings[1]);
  };
  /**
   * 매수 우선순위
   */
  const [checkedListCondition, setCheckedListCondition] = useState([]);

  //조건 당 div
  const OfferBox = styled.div`
    box-shadow: 0px 0px 7px 3px ${(props) => props.color};
    margin: 10px;
    padding: 15px 20px 10px 20px;
    width: 95%;
    height: 70px;
    align-items: center;
    display: inline-block;
  `;
  //조건 checkbox 함수
  const [disabledPER, setDisabledPER] = useState(false);
  const [disabledPBR, setDisabledPBR] = useState(true);
  const [disabledPSR, setDisabledPSR] = useState(true);
  const [disabledROE, setDisabledROE] = useState(true);
  const [disabledROA, setDisabledROA] = useState(true);
  const [disabledNum, setdisabledNum] = useState(1);

  //조건 [min, max, order]
  const [PER, setPER] = useState([-100, 300, 1]);
  const [PBR, setPBR] = useState([0.1, 300, 2]);
  const [PSR, setPSR] = useState([0.1, 300, 3]);
  const [ROE, setROE] = useState([-200, 200, 4]);
  const [ROA, setROA] = useState([-200, 200, 5]);

  const onChangeCondition = (checkedValues) => {
    console.log("value?", checkedValues);
    console.log("체크된수", checkedValues.length);
    setCheckedListCondition(checkedValues);
    setdisabledNum(checkedValues.length);
    console.log("이펙트 실행");
    console.log("disabledNum", checkedValues.length);
    if (!disabledPER && PER[2] > checkedValues.length) {
      // setPER([PER[0], PER[1], disabledNum]);
      onChangeOrderPER(checkedValues.length);
    } else if (!disabledPBR && PBR[2] > checkedValues.length) {
      console.log("찾음");
      // setPBR([PBR[0], PBR[1], disabledNum]);
      onChangeOrderPBR(checkedValues.length);
    } else if (!disabledPSR && PSR[2] > checkedValues.length) {
      // setPSR([PSR[0],PSR[1],disabledNum]);
      onChangeOrderPSR(checkedValues.length);
    } else if (!disabledROE && ROE[2] > checkedValues.length) {
      console.log("알아냄", checkedValues.length);
      onChangeOrderROE(checkedValues.length);
    } else if (!disabledROA && ROA[2] > checkedValues.length) {
      onChangeOrderROA(checkedValues.length);
    } else return;
  };

  const onChangeCon = (e) => {
    const val = e.target.value;

    if (val === "PER") {
      setDisabledPER(!e.target.checked);
    } else if (val === "PBR") {
      setDisabledPBR(!e.target.checked);
    } else if (val === "PSR") {
      setDisabledPSR(!e.target.checked);
    } else if (val === "ROE") {
      setDisabledROE(!e.target.checked);
    } else {
      setDisabledROA(!e.target.checked);
    }
  };
  useEffect(() => {
    console.log("diable", disabledPER);
  }, [onChangeCon]);

  useEffect(() => {
    console.log("list?", checkedListCondition);
    console.log("num?", disabledNum);
  }, [onChangeCondition]);

  //조건 범위(range slider)
  const [perval, setperval] = useState([]);
  const onChangeRange = (value) => {};

  //우선순위
  const onChangeOrderPER = (value) => {
    onChangeCondition(checkedListCondition);
    var checkOrder = [PBR[2], PSR[2], ROE[2], ROA[2]].indexOf(value);
    switch (checkOrder) {
      case 0:
        setPBR([PBR[0], PBR[1], PER[2]]);
        break;
      case 1:
        setPSR([PSR[0], PSR[1], PER[2]]);
        break;
      case 2:
        setROE([ROE[0], ROE[1], PER[2]]);
        break;
      case 3:
        setROA([ROA[0], ROA[1], PER[2]]);
        break;
      default:
        return;
    }
    setPER([PER[0], PER[1], value]);
  };
  const onChangeOrderPBR = (value) => {
    onChangeCondition(checkedListCondition);
    var checkOrder = [PER[2], PSR[2], ROE[2], ROA[2]].indexOf(value);
    switch (checkOrder) {
      case 0:
        setPER([PER[0], PER[1], PBR[2]]);
        break;
      case 1:
        setPSR([PSR[0], PSR[1], PBR[2]]);
        break;
      case 2:
        setROE([ROE[0], ROE[1], PBR[2]]);
        break;
      case 3:
        setROA([ROA[0], ROA[1], PBR[2]]);
        break;
      default:
        return;
    }
    setPBR([PBR[0], PBR[1], value]);
  };
  const onChangeOrderPSR = (value) => {
    onChangeCondition(checkedListCondition);
    var checkOrder = [PER[2], PBR[2], ROE[2], ROA[2]].indexOf(value);
    switch (checkOrder) {
      case 0:
        setPER([PER[0], PER[1], PSR[2]]);
        break;
      case 1:
        setPBR([PBR[0], PBR[1], PSR[2]]);
        break;
      case 2:
        setROE([ROE[0], ROE[1], PSR[2]]);
        break;
      case 3:
        setROA([ROA[0], ROA[1], PSR[2]]);
        break;
      default:
        return;
    }
    setPSR([PSR[0], PSR[1], value]);
  };
  const onChangeOrderROE = (value) => {
    onChangeCondition(checkedListCondition);
    var checkOrder = [PER[2], PBR[2], PSR[2], ROA[2]].indexOf(value);
    switch (checkOrder) {
      case 0:
        setPER([PER[0], PER[1], ROE[2]]);
        break;
      case 1:
        setPBR([PBR[0], PBR[1], ROE[2]]);
        break;
      case 2:
        setPSR([PSR[0], PSR[1], ROE[2]]);
        break;
      case 3:
        setROA([ROA[0], ROA[1], ROE[2]]);
        break;
      default:
        return;
    }
    setROE([ROE[0], ROE[1], value]);
  };
  const onChangeOrderROA = (value) => {
    onChangeCondition(checkedListCondition);
    var checkOrder = [PER[2], PBR[2], PSR[2], ROE[2]].indexOf(value);
    console.log("checkOrder", checkOrder);
    switch (checkOrder) {
      case 0:
        setPER([PER[0], PER[1], ROA[2]]);
        break;
      case 1:
        setPBR([PBR[0], PBR[1], ROA[2]]);
        break;
      case 2:
        setPSR([PSR[0], PSR[1], ROA[2]]);
        break;
      case 3:
        setROE([ROE[0], ROE[1], ROA[2]]);
        break;
      default:
        return;
    }
    setROA([ROA[0], ROA[1], value]);
  };
  /**
   * Panel custom
   */
  const customPanelStyle = {
    color: "#f7f7f7",
    borderRadius: 4,
    marginBottom: 24,
    border: 0,
    overflow: "hidden",
  };
  /**
   * 매도조건 sellMinCondition
   */
  const [sellMin, setsellMin] = useState(-10);
  const [sellMax, setsellMax] = useState(10);

  /**
   * submit 제출, post
   * */
  const [ActiveKey, setActiveKey] = useState(["1", "2", "3", "4"]);
  const submit = () => {
    setActiveKey([]);
    document.documentElement.scrollTo(0, 0);
    const market = [];
    if (kospiCode) {
      market.push(1);
    }
    if (kosdaqCode) {
      market.push(2);
    }
    if (market.length < 1) {
      console.log("마켓없음!!!!");
      return;
    }

    var sector = [];
    if (checkedListKosdaq) {
      sector = checkedListKospi.concat(checkedListKosdaq);
    } else {
      checkedListKospi.map((ko) => sector.push(ko));
    }

    const conditions = [];
    if (!disabledPER) {
      const PERdata = [
        window.localStorage.getItem("PERMIN"),
        window.localStorage.getItem("PERMAX"),
        PER[2],
      ];
      conditions.push({ per: PERdata });
    }
    if (!disabledPBR) {
      const PBRdata = [
        window.localStorage.getItem("PBRMIN"),
        window.localStorage.getItem("PBRMAX"),
        PBR[2],
      ];
      conditions.push({ pbr: PBRdata });
    }
    if (!disabledPSR) {
      const PSRdata = [
        window.localStorage.getItem("PSRMIN"),
        window.localStorage.getItem("PSRMAX"),
        PSR[2],
      ];
      conditions.push({ psr: PSRdata });
    }
    if (!disabledROE) {
      const ROEdata = [
        window.localStorage.getItem("ROEMIN"),
        window.localStorage.getItem("ROEMAX"),
        ROE[2],
      ];
      conditions.push({ roe: ROEdata });
    }
    if (!disabledROA) {
      const ROAdata = [
        window.localStorage.getItem("ROAMIN"),
        window.localStorage.getItem("ROAMAX"),
        ROA[2],
      ];
      conditions.push({ roa: ROAdata });
    }
    console.log(conditions);
    const data = {
      id: window.sessionStorage.getItem("id"),
      start: start,
      end: end,
      market: market,
      sector: sector,
      sellCondition: [sellMin, sellMax],
      conditions: conditions,
    };

    Testing(data);
    const SpinDiv = styled.div`
      padding: 200px 0 0 300px;
    `;
    setView(
      <SpinDiv>
        <Spin tip="테스트 중입니다..."></Spin>
      </SpinDiv>
    );
  };
  async function Testing(values) {
    console.log("vals", values);
    await axios
      .post(
        "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/bt/",
        values
      )
      .catch(function (error) {
        console.log(error);
      })
      .then((response) => {
        console.log("백테스팅res", response.data);
        BacktestBar(response.data);
      });
  }

  const [Btdata, setBtdata] = useState({});
  const history = useHistory();
  const BacktestBar = (data) => {
    const arr = [];
    let i = 0;
    const btarr = data;
    const totalarr = [];
    console.log("Btarr", btarr);
    for (var key in btarr) {
      if (key == "error") {
        history.push("/main/backtest?code=none");
      }
      console.log("key", key);
      if (i == 0) {
        console.log("data", btarr[key], key);
        if (btarr[key] != 0) {
          arr.push({
            date: key,
            profit: btarr[key],
            sum: 0,
          });
        }
      } else if (key == "total") {
        totalarr.push({ date: "총 수익률", profit: btarr[key] });
      } else {
        if (btarr[key] != 0) {
          console.log("data", btarr[key], key);
          arr.push({
            date: key,
            profit: btarr[key],
          });
        }
      }
      i++;
    }
    arr.push(totalarr[0]);
    const btdataset = [];

    var sum = 0;
    arr.map((a, idx) => {
      if (idx != 0) {
        btdataset.push({
          date: a.date,
          수익률: a.profit,
          누적수익률: `${a.profit + sum}`,
        });
        sum = a.profit + sum;
        console.log(
          "수익률,누적수익률",
          a.profit,
          a.profit + arr[idx - 1].profit
        );
      } else {
        sum = a.profit;
        btdataset.push({
          date: a.date,
          수익률: a.profit,
          누적수익률: sum,
        });
      }
    });
    console.log("btdataset arr", btdataset);
    setBtdata(btdataset);
  };

  useEffect(() => {
    if (Btdata.length > 0) {
      setActiveKey(["1", "2", "3", "4"]);
      setView(
        <BarChart width={730} height={400} data={Btdata}>
          <XAxis dataKey="date" stroke="#EAF0F4" />
          <ReferenceLine y={0} stroke="white" />
          <YAxis tickFormatter={(label) => label + " %"} stroke="#EAF0F4" />
          <Tooltip
            formatter={(label) => label + " (%)"}
            cursor={{ stroke: "white", fill: "none" }}
          />
          <Bar maxBarSize={30} dataKey="수익률" fill="#ffde4e" />
          <Bar maxBarSize={30} dataKey="누적수익률" fill="#ff9100" />
        </BarChart>
      );
    } else {
      setView(DoIntBox);
    }
  }, [Btdata]);
  const DoIntBox = () => {
    return (
      <BoxWrapper w="700px" padding="100px 0 30px 30%">
        <MText
          font="a고딕15"
          size="30px"
          display="inline-flex"
          padBot="0"
          color="#f05454"
        >
          백테스팅
        </MText>
        <br />
        <MText font="a고딕13" size="30px" color="#dddddd">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;조건을 입력하여
          실행
        </MText>
        <br />
        <MText
          font="a고딕13"
          size="40px"
          color="#dddddd"
          className="fadeInDown animated"
          padding="30px 50px 0 150px"
        >
          <ArrowDownOutlined />
        </MText>
      </BoxWrapper>
    );
  };
  const [view, setView] = useState(DoIntBox);
  const [btData, setbtData] = useState(window.localStorage.getItem("btData"));

  const Collapse2 = styled(Collapse)`
    overflow-y: scroll;
    max-height: 500px;
  `;
  return (
    <Wrapper>
      <BoxWrapper w="45%">
        <ConditionWrapper>
          <Collapse
            className="collapse"
            defaultActiveKey={["1", "2", "3", "4"]}
          >
            <Panel header="기간설정" key="1" className="collapse-panel">
              <Space direction="vertical" size={12}>
                <RangePicker
                  disabledDate={disabledDate}
                  onChange={updateDate}
                />
              </Space>
            </Panel>
            <Panel header={sectorPanel} key="2" className="collapse-panel">
              <p>코스피</p>
              <Checkbox
                indeterminate={indeterminateKospi}
                onChange={onCheckAllChangeKospi}
                checked={checkAllKospi}
              >
                전체선택
              </Checkbox>
              <CheckboxGroup
                options={KospiSector}
                value={checkedListKospi}
                onChange={onChangeKospi}
              />
              <Divider></Divider>
              <p>코스닥</p>
              <Checkbox
                indeterminate={indeterminateKosdaq}
                onChange={onCheckAllChangeKosdaq}
                checked={checkAllKosdaq}
              >
                전체선택
              </Checkbox>
              <CheckboxGroup
                options={KosdaqSector}
                value={checkedListKosdaq}
                onChange={onChangeKosdaq}
              />
            </Panel>
            <Panel header="매수 우선순위" key="3" className="collapse-panel">
              <Checkbox.Group
                style={{ width: "100%" }}
                onChange={onChangeCondition}
                defaultValue={["PER"]}
              >
                <OfferBox color={disabledPER ? "#ababab" : "#1890ff"}>
                  <Row>
                    <Col span={6}>
                      <Checkbox value="PER" onChange={onChangeCon}>
                        PER
                      </Checkbox>
                    </Col>
                    <Col span={6}>
                      우선순위&nbsp;
                      <InputNumber
                        min={1}
                        max={disabledNum}
                        style={{ width: 50 }}
                        value={PER[2]}
                        onChange={onChangeOrderPER}
                        disabled={disabledPER}
                      />
                    </Col>
                    <Col span={12}>
                      <Slider
                        disabled={disabledPER}
                        range
                        marks={{ "-100": "-100", 300: "300" }}
                        min={-100}
                        max={300}
                        defaultValue={[-90, 290]}
                        onChange={onChangeRange}
                        onAfterChange={(value) => {
                          console.log("afterChangePER", value);
                          window.localStorage.removeItem("PERMIN");
                          window.localStorage.removeItem("PERMAX");
                          window.localStorage.setItem("PERMIN", value[0]);
                          window.localStorage.setItem("PERMAX", value[1]);
                        }}
                      />
                    </Col>
                  </Row>
                </OfferBox>
                <OfferBox color={disabledPBR ? "#ababab" : "#1890ff"}>
                  <Row>
                    <Col span={6}>
                      <Checkbox value="PBR" onChange={onChangeCon}>
                        PBR
                      </Checkbox>
                    </Col>
                    <Col span={6}>
                      우선순위&nbsp;
                      <InputNumber
                        min={1}
                        max={disabledNum}
                        style={{ width: 50 }}
                        value={disabledPBR ? "" : PBR[2]}
                        onChange={onChangeOrderPBR}
                        disabled={disabledPBR}
                      />
                    </Col>
                    <Col span={12}>
                      <Slider
                        disabled={disabledPBR}
                        range
                        marks={{ 0.1: "0.1", 300: "300" }}
                        step={0.1}
                        min={0.1}
                        max={300}
                        defaultValue={[0.1, 300]}
                        onChange={onChangeRange}
                        onAfterChange={(value) => {
                          console.log("afterChangePBR", value);
                          window.localStorage.removeItem("PBRMIN");
                          window.localStorage.removeItem("PBRMAX");
                          window.localStorage.setItem("PBRMIN", value[0]);
                          window.localStorage.setItem("PBRMAX", value[1]);
                        }}
                      />
                    </Col>
                  </Row>
                </OfferBox>
                <OfferBox color={disabledPSR ? "#ababab" : "#1890ff"}>
                  <Row>
                    <Col span={6}>
                      <Checkbox value="PSR" onChange={onChangeCon}>
                        PSR
                      </Checkbox>
                    </Col>
                    <Col span={6}>
                      우선순위&nbsp;
                      <InputNumber
                        min={1}
                        max={disabledNum}
                        style={{ width: 50 }}
                        value={disabledPSR ? "" : PSR[2]}
                        onChange={onChangeOrderPSR}
                        disabled={disabledPSR}
                      />
                    </Col>
                    <Col span={12}>
                      <Slider
                        disabled={disabledPSR}
                        range
                        marks={{ 0.1: "0.1", 300: "300" }}
                        step={0.1}
                        min={0.1}
                        max={300}
                        defaultValue={[0.1, 300]}
                        onChange={onChangeRange}
                        onAfterChange={(value) => {
                          window.localStorage.removeItem("PSRMIN");
                          window.localStorage.removeItem("PSRMAX");
                          window.localStorage.setItem("PSRMIN", value[0]);
                          window.localStorage.setItem("PSRMAX", value[1]);
                        }}
                      />
                    </Col>
                  </Row>
                </OfferBox>
                <OfferBox color={disabledROE ? "#ababab" : "#1890ff"}>
                  <Row>
                    <Col span={6}>
                      <Checkbox value="ROE" onChange={onChangeCon}>
                        ROE (단위:%)
                      </Checkbox>
                    </Col>
                    <Col span={6}>
                      우선순위&nbsp;
                      <InputNumber
                        min={1}
                        max={disabledNum}
                        style={{ width: 50 }}
                        value={disabledROE ? "" : ROE[2]}
                        onChange={onChangeOrderROE}
                        disabled={disabledROE}
                      />
                    </Col>
                    <Col span={12}>
                      <Slider
                        disabled={disabledROE}
                        range
                        marks={{ "-200": "-200%", 200: "200%" }}
                        step={10}
                        min={-200}
                        max={200}
                        defaultValue={[-200, 200]}
                        onChange={onChangeRange}
                        onAfterChange={(value) => {
                          window.localStorage.removeItem("ROEMIN");
                          window.localStorage.removeItem("ROEMAX");
                          window.localStorage.setItem("ROEMIN", value[0]);
                          window.localStorage.setItem("ROEMAX", value[1]);
                        }}
                      />
                    </Col>
                  </Row>
                </OfferBox>
                <OfferBox color={disabledROA ? "#ababab" : "#1890ff"}>
                  <Row>
                    <Col span={6}>
                      <Checkbox value="ROA" onChange={onChangeCon}>
                        ROA (단위:%)
                      </Checkbox>
                    </Col>
                    <Col span={6}>
                      우선순위&nbsp;
                      <InputNumber
                        min={1}
                        max={disabledNum}
                        style={{ width: 50 }}
                        value={disabledROA ? "" : ROA[2]}
                        onChange={onChangeOrderROA}
                        disabled={disabledROA}
                      />
                    </Col>
                    <Col span={12}>
                      <Slider
                        disabled={disabledROA}
                        range
                        marks={{ "-200": "-200%", 200: "200%" }}
                        step={10}
                        min={-200}
                        max={200}
                        defaultValue={[-200, 200]}
                        onChange={onChangeRange}
                        onAfterChange={(value) => {
                          window.localStorage.removeItem("ROAMIN");
                          window.localStorage.removeItem("ROAMAX");
                          window.localStorage.setItem("ROAMIN", value[0]);
                          window.localStorage.setItem("ROAMAX", value[1]);
                        }}
                      />
                    </Col>
                  </Row>
                </OfferBox>
              </Checkbox.Group>
            </Panel>
            <Panel header="매도조건" key="4" className="collapse-panel">
              최소&nbsp;:&nbsp;
              <InputNumber
                min={-100}
                max={100}
                style={{ width: 50 }}
                value={sellMin}
                onChange={(value) => setsellMin(value)}
              />
              &nbsp;%&nbsp;&nbsp; 최대&nbsp;:&nbsp;
              <InputNumber
                min={-100}
                max={100}
                style={{ width: 50 }}
                value={sellMax}
                onChange={(value) => setsellMax(value)}
              />
              &nbsp;%&nbsp;
            </Panel>
          </Collapse>
          <ButtonWrapper className="btn">
            <Button type="primary" className="SubmitBtn" onClick={submit}>
              테스트 하기
            </Button>
          </ButtonWrapper>
        </ConditionWrapper>
      </BoxWrapper>
      <BoxWrapper padding="100px 10px 0 0">{view}</BoxWrapper>
    </Wrapper>
  );
};

export default Backtest;

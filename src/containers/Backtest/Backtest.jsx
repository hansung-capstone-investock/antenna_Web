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
} from "antd";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";
import moment from "moment";
import React, { useState, useEffect } from "react";
import "./Backtest.css";

const { Panel } = Collapse;
const { RangePicker } = DatePicker;

const Backtest = () => {
  const [start, setstart] = useState();
  const [end, setend] = useState();

  const user = window.sessionStorage.getItem("id");

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
   * 시장구분 Checkbox : name, code 반환
   */

  return (
    <div>
      <Space direction="vertical" size={12}>
        <RangePicker disabledDate={disabledDate} onChange={updateDate} />
      </Space>

      <Collapse className="collapse">
        <Panel header="시장구분" key="1" className="collapse-panel">
          <p>냥?</p>
        </Panel>
        <Panel header="업종" key="2" className="collapse-panel">
          <p>냥?</p>
        </Panel>
      </Collapse>
    </div>
  );
};

export default Backtest;

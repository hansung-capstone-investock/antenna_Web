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
} from "recharts";
import { Table, Tag, Space } from "antd";

const StockChart = (data) => {
  const ChartWrapper = styled.div`
    width: 450px;
    height: 200px;
    //오늘의 증시 보러가기 텍스트 때문에 margin
    margin-bottom: 60px;
  `;
  const arr = [];
  const starr = data.stockData;
  starr.map((st, idx) => {
    arr.push({ date: st.date, close: st.close });
  });
  console.log("arr chart", arr);
  return (
    <ChartWrapper>
      <ResponsiveContainer width="200px" height="500px">
        <LineChart
          width={600}
          height={300}
          data={arr}
          margin={{
            top: 5,
            right: 10,
            left: 0,
            bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="4 4" />
          <XAxis dataKey="date" tick={{ fontSize: 10 }} />
          <YAxis
            dataKey="close"
            type="number"
            domain={["auto", "auto"]}
            tick={{ fontSize: 10 }}
          />
          <Tooltip formatter={(val, name) => [val, "종가"]} />
          <Line type="monotone" dataKey="close" stroke="#8884d8" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
};
export default StockChart;

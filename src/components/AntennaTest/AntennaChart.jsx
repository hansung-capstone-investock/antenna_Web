import React, { useState, useEffect, PureComponent } from "react";
import { ResponsiveLine } from "nivo";
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

const AntennaChart = (data) => {
  const predict = data.predict;
  const preIdx = Object.keys(predict);
  console.log("predict idx", preIdx);
  const preData = Object.values(predict);
  console.log("predict vals", preData);
  const preArr = [];
  preIdx.map((key, idx) => {
    preArr.push({ key: key, data: preData[idx] });
  });

  const actual = data.actual;
  const actIdx = Object.keys(actual);
  const actData = Object.values(actual);

  return (
    <ResponsiveContainer width="100%" height="100%">
      <LineChart
        width={600}
        height={300}
        data={preArr}
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
          dataKey="closeY"
          type="number"
          domain={["auto", "auto"]}
          tick={{ fontSize: 10 }}
        />
        <Tooltip formatter={(val, name) => [val, "예측치"]} />
        <Line type="monotone" dataKey="close" stroke="#f75283" dot={false} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default AntennaChart;

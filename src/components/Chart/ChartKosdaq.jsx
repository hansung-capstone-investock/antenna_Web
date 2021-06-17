import React, { useState, useEffect, PureComponent } from "react";
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

const ChartKosdaq = () => {
  const [Kosdaq, setKosdaq] = useState([]);
  useEffect(() => {
    const fetchKosdaq = async () => {
      const res = await axios.get(
        "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/kosdaqyear/",
        (req, res) => {
          req.header("Access-Control-Allow-Origin", "*");
          res.header("Access-Control-Allow-Origin", "*");
        }
      );
      setKosdaq(res.data);
      console.log("res kosdaq", res.data);
      window.localStorage.setItem(
        "todayKosdaq",
        res.data[res.data.length - 1].close
      );
      window.localStorage.setItem(
        "lastKosdaq",
        res.data[res.data.length - 2].close
      );
    };
    fetchKosdaq();
  }, []);
  const arr = [];
  Kosdaq.map((a) => {
    arr.push({
      date: a.date.substr(2, 8),
      close: a.close,
      closeY: Math.floor(a.close),
    });
  });
  return (
    <ResponsiveContainer width="100%" height="100%">
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
          dataKey="closeY"
          type="number"
          domain={["auto", "auto"]}
          tick={{ fontSize: 10 }}
        />
        <Tooltip formatter={(val, name) => [val, "코스닥"]} />
        <Line type="monotone" dataKey="close" stroke="#f75288" dot={false} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default ChartKosdaq;

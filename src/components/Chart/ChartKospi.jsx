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

const ChartKospi = () => {
  const [Kospi, setKospi] = useState([]);
  useEffect(() => {
    const fetchKospi = async () => {
      const res = await axios.get(
        "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/kospiyear/",
        (req, res) => {
          req.header("Access-Control-Allow-Origin", "*");
          res.header("Access-Control-Allow-Origin", "*");
        }
      );
      setKospi(res.data);
      console.log("res kospi data", res.data);
      console.log("res data todaykospi", res.data[res.data.length - 1]);
      console.log("res data lastkospi", res.data[res.data.length - 2]);
      window.localStorage.setItem(
        "todayKospi",
        res.data[res.data.length - 1].close
      );
      window.localStorage.setItem(
        "lastKospi",
        res.data[res.data.length - 2].close
      );
    };
    fetchKospi();
  }, []);
  const arr = [];
  Kospi.map((a) => {
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
        <Tooltip formatter={(val, name) => [val, "코스피"]} />
        <Line type="monotone" dataKey="close" stroke="#f75283" dot={false} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default ChartKospi;

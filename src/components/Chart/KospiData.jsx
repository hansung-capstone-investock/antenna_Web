// import React, { useState, useEffect, useCallback } from "react";
// import axios from "axios";
// import styled from "styled-components";
// import { List } from "antd";
// import {
//   LineChart,
//   Line,
//   XAxis,
//   YAxis,
//   CartesianGrid,
//   Tooltip,
//   Legend,
// } from "recharts";

// function KospiData() {
//   const ItemWrapper = styled.div`
//     margin: 1px;
//     .ant-list-item-meta-description {
//       overflow: hidden;
//       white-space: nowrap;
//       text-overflow: ellipsis;
//     }
//   `;

//   const Wrapper = styled.div`
//     width: calc(100%);
//   `;

//   const [Kospi, setKospi] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     const fetchKospi = async () => {
//       try {
//         setError(null);
//         setKospi(null);
//         setLoading(true);
//         const response = await axios.get(
//           "http://ec2-13-125-236-101.ap-northeast-2.compute.amazonaws.com:8000/stock/kospiyear/",
//           (req, res) => {
//             req.header("Access-Control-Allow-Origin", "*");
//             res.header("Access-Control-Allow-Origin", "*");
//           }
//         );
//         setKospi(response.data); // 데이터는 response.data 안에 들어있습니다.
//       } catch (e) {
//         setError(e);
//       }
//       setLoading(false);
//     };

//     fetchKospi();
//   }, []);

//   if (!Kospi) return null;

//   const datas = [];

//   Kospi.map((kospi) => datas.push([kospi.date, kospi.close]));

//   return Kospi;
// }

// export default KospiData;

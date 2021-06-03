import React, { useState, useEffect } from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";

import axios from "axios";

const Wrapper = styled.div`
  width: 280px;
  height: 235px;
  border: 6px black solid;
  padding-left: 10px;
  padding-right: 10px;

  @media screen and (max-width: 1300px) {
    display: inline-block;
    margin: 0 0 0 30px;
    width: 416px;
  }
`;

const HotKeyWord = () => {
  const [dc, setdc] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchHword = async () => {
      try {
        setError(null);
        setdc(null);
        setLoading(true);
        const response = await axios.get(
          "http://ec2-13-125-236-101.ap-northeast-2.compute.amazonaws.com:8000/views/api/dcList",
          (req, res) => {
            req.header("Access-Control-Allow-Origin", "*");
            res.header("Access-Control-Allow-Origin", "*");
          }
        );
        setdc(response.data); // 데이터는 response.data 안에 들어있습니다.
        console.log("dc", dc);
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };

    fetchHword();
  }, []);

  return <Wrapper>/</Wrapper>;
};

export default HotKeyWord;

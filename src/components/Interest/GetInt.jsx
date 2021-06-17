import React, { useState, useEffect, useCallback } from "react";
import { Redirect, Route, useHistory } from "react-router-dom";
import axios from "axios";
import styled from "styled-components";
import { List, Avatar } from "antd";

function GetInt(values) {
  const id = values;
  const [data, setData] = useState({});
  axios
    .post(
      "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/account/api/intereststock/",
      {
        name: id,
      },
      { headers: { "Content-Type": "application/json" } }
    )
    .catch(function (error) {
      console.log(error);
    })
    .then((response) => {
      console.log("관심종목==> ", response);
      const data = response.data;
    });
  return data;
}

export default GetInt;

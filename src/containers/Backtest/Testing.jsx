import React, { useState, useEffect, useCallback } from "react";
import { Redirect, Route, useHistory } from "react-router-dom";
import axios from "axios";
import styled from "styled-components";
import { List, Avatar } from "antd";

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
      console.log("백테스팅res", response);
    });
}

export default Testing;

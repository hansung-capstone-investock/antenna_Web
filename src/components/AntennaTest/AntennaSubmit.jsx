import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import styled from "styled-components";
import { AntennaChart } from "../../components";

async function AntennaSubmit(data) {
  const response = await axios.post(
    "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/tensor/antenna/",
    data
  );
  console.log("Antenna", response.data);
  console.log("나온다...", response.data.actual);
  AntennaChart(response.data);

  window.localStorage.setItem("antSubmit", "done");
  return;
}

export default AntennaSubmit;

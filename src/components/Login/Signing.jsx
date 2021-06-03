import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import styled from "styled-components";
import { List, Avatar } from "antd";

function Signing(values) {
  const id = values.user.id;
  const password = values.user.pw;

  console.log(values.user.id);

  axios({
    url:
      "http://ec2-13-125-236-101.ap-northeast-2.compute.amazonaws.com:8000/account/api/signup/",
    method: "post",
    data: { id, password },
    headers: {
      "content-type": "application/json",
    },
  });

  if (!id) return null;

  return <div></div>;
}

export default Signing;

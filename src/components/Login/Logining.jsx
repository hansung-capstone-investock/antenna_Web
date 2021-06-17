import React, { useState, useEffect, useCallback } from "react";
import { Redirect, Route, useHistory } from "react-router-dom";
import axios from "axios";
import styled from "styled-components";
import { List, Avatar } from "antd";

function Logining(values) {
  const id = values.id;
  const password = values.pw;
  axios
    .post(
      "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/account/api/login/",
      {
        id: id,
        password: password,
      }
    )
    .catch(function (error) {
      console.log(error);
    })
    .then((response) => {
      console.log(response);
      const data = response.data;

      if (data.code === "1001") {
        console.log("로그인실패");
        return false;
      } else {
        console.log("로그인성공");
        window.sessionStorage.setItem("id", id);
        window.sessionStorage.setItem("pw", password);
        window.sessionStorage.setItem("logged", "true");

        document.location.href = "/main/antenna";
      }
    });
}

export default Logining;

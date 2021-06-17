import React from "react";
import styled from "styled-components";
import { SwapRightOutlined } from "@ant-design/icons";
import { Link, useHistory } from "react-router-dom";

//메인의 관심종목 박스
const Box = styled.div`
  height: 100%;
  width: 100%;
  padding: 12% 5px 80px 15%;
`;
const GotoPage = styled(Link)`
  text-decoration: none;
  font-family: "nanumRoundB";
  font-weight: 600;
  color: #f14b4b;
  font-size: 16px;
`;
const ItemBox = () => {
  const history = useHistory();
  console.log("path", history.location.pathname);

  const logged = window.sessionStorage.getItem("logged");

  return (
    <Box>
      {logged ? (
        <div>hi</div>
      ) : (
        <GotoPage to="/main/infoThresh">
          로그인하고 관심종목 설정하기 <SwapRightOutlined />
        </GotoPage>
      )}
    </Box>
  );
};

export default ItemBox;

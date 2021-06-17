import React, { useContext } from "react";
import styled, { css, ThemeContext } from "styled-components";
import { Link, useHistory } from "react-router-dom";
import { MainText } from "../../components";
import { MText } from "../../components";
import "./MainBox.css";

const withPathName = (Component) => (props) => {
  const history = useHistory();
  return <Component {...props} path={history.location.pathname} />;
};

const MenuItem = withPathName(styled(Link)`
  font-family: "Mfont";
  font-size: 24px;
  font-weight: 600;
  margin-top: 200px;
  margin-right: 10px;
  padding: 0px 10px;
  text-decoration: none;
  text-align: right;
  color: ${(props) => props.theme.fontColor};
  height: 40px;
  display: inline-block;
  position: relative;
  ::after {
    position: absolute;
    bottom: 5px;
    left: 0px;
    height: 5px;
    width: 0px;
    background-color: #30475e;
    content: "";
    transition: 0.2s;
  }
  &:hover {
    ::after {
      text-decoration: wavy;
      width: 100%;
    }
  }
`);
const imgsrc = "/AntennaGif.gif";

const Wrapper = styled.div``;

const Box = styled.div`
  padding: 80px 60px;
  display: inline-block;
  height: 500px;
  width: 100%;
  background-image: url(${imgsrc});
  background-size: cover;
  background-position: center;
`;
const Tdiv = styled.div`
  text-shadow: ${(props) => props.shadow || ""};
  color: ${(props) => props.color || ""};
`;

const MainBox = () => {
  return (
    <div>
      <Box>
        <MainText
          font="a아시아헤드2"
          color="#f14b4b"
          className="fadeIn animated"
        >
          <Tdiv>ANTENNA</Tdiv>
        </MainText>
        <MText color="#30475e" size="18px" className="fadeIn animated">
          개미들을 위한 로보 어드바이저
        </MText>
        <br />
        <MenuItem to="/main/antenna">
          <Tdiv color="#30475e">C l i c k ! > ></Tdiv>
        </MenuItem>
      </Box>
    </div>
  );
};

export default MainBox;

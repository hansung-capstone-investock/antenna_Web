import React, { useContext } from "react";
import styled, { css, ThemeContext } from "styled-components";
import { Link, useHistory } from "react-router-dom";
import { MainText } from "../../components";
import { MText } from "../../components";

const withPathName = (Component) => (props) => {
  const history = useHistory();
  return <Component {...props} path={history.location.pathname} />;
};

const MenuItem = withPathName(styled(Link)`
  font-size: 16px;
  font-weight: 600;
  margin-top: 60px;
  float: right;
  padding: 0px 10px;
  text-decoration: none;
  text-align: right;
  color: ${(props) => props.theme.fontColor};
  height: 40px;
  display: inline-block;
  position: relative;
  ::after {
    position: absolute;
    bottom: 10px;
    left: 0px;
    height: 3px;
    width: 0px;
    background-color: red;
    content: "";
    transition: 0.3s;
  }
  &:hover {
    ::after {
      width: 100%;
    }
  }
  ${(props) => {
    if (props.path === props.to) {
      return css`
        ::after {
          width: 100%;
        }
      `;
    }
  }}
`);
const imgsrc = "/AntImg.gif";

const Wrapper = styled.div``;

const Box = styled.div`
  margin: 100px 60px 0 60px;
  padding: 60px;
  display: inline-block;
  height: 400px;
  width: 400px;
  box-shadow: 5px 5px 5px 5px gray;

  background-image: url(${imgsrc});
  background-size: cover;
  background-position: center;

  @media screen and (max-width: 1100px) {
    position: inherit;
    display: block;
    height: 600px;
    width: 100%;
    margin: 0 0 0 0;
  }
  @media screen and (max-height: 600px) {
    position: inherit;
    display: block;
    height: 600px;
    width: 100%;
    margin: 0 0 0 0;
  }
`;

const MainBox = () => {
  return (
    <div>
      <Box>
        <MainText>Antenna</MainText>
        <MText>개미들을 위한 로보 어드바이저</MText>
        <br />
        <MenuItem to="/main/antenna">자세히보기</MenuItem>
      </Box>
    </div>
  );
};

export default MainBox;

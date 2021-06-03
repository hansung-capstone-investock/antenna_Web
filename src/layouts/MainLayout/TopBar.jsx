import React, { useContext } from "react";
import { Link, useHistory } from "react-router-dom";
import styled, { css, ThemeContext } from "styled-components";
import { Search } from "../../components";
import { EyeFilled, LoginOutlined } from "@ant-design/icons";
import { MenuItems } from "../../containers/MenuItems";

const withPathName = (Component) => (props) => {
  const history = useHistory();
  return <Component {...props} path={history.location.pathname} />;
};

const Logo = styled.div`
  height: 50px;
  font-size: 30px;
  font-weight: bold;
  padding: 0px 20px;
  cursor: pointer;
  color: ${(props) => props.theme.fontColor};
`;

const Wrapper = styled.div`
  width: 100%;
  height: 80px;
  display: flex;
  overflow: hidden;
  align-items: center;
  background-color: ${(props) => props.theme.bgColor};
  box-shadow: 0 1px 3px 0 rgb(0 0 0 / 12%);
  user-select: none;
`;

const PrettyOfWhiteSpace = styled.div`
  flex: 1;
  height: 100%;
`;

const MenuItem = withPathName(styled(Link)`
  font-size: 26px;
  font-weight: 600;
  padding: 0px 16px;
  text-decoration: none;
  color: ${(props) => props.theme.fontColor};
  line-height: 70px;
  height: 70px;
  display: inline-block;
  position: relative;
  margin: 0px 10px;
  ::after {
    position: absolute;
    bottom: 10px;
    left: 0px;
    height: 3px;
    width: 0px;
    background-color: ${(props) => props.theme.primaryColor};
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

  @media screen and (max-width:1100px) {
    display: none;
  }
`);

const LoginItem = withPathName(styled(Link)`
  font-size: 26px;
  font-weight: 600;
  padding: 0px 16px;
  text-decoration: none;
  color: ${(props) => props.theme.fontColor};
  line-height: 70px;
  height: 70px;
  display: inline-block;
  position: relative;
  margin: 0px 10px;
  ::after {
    position: absolute;
    bottom: 10px;
    left: 0px;
    height: 3px;
    width: 0px;
    background-color: ${(props) => props.theme.primaryColor};
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
const ThemeButton = styled.div`
  height: 30px;
  width: 30px;
  margin: 0px 16px;
  color: ${(props) => props.theme.fontColor};
  border-radius: 12px;
  text-align: center;
  font-size: 22px;
  cursor: pointer;
  &:hover {
    opacity: 0.8;
  }
`;

const TopBar = (props) => {
  const logged = window.sessionStorage.getItem("logged");
  console.log("logged??", logged);

  const history = useHistory();

  return (
    <Wrapper>
      <Logo onClick={() => history.push("/main/home")}>Investock</Logo>
      <PrettyOfWhiteSpace />
      <div>
        <MenuItem to="/main/antenna">Antenna</MenuItem>
        <MenuItem to="/main/news">뉴스</MenuItem>
        <MenuItem to="/main/infoThresh">투자정보</MenuItem>
        <MenuItem to="/main/backtest">백테스트</MenuItem>
        <MenuItems></MenuItems>
      </div>
      {logged === "true" ? (
        <LoginItem to="/main/myPage">마이페이지</LoginItem>
      ) : (
        <LoginItem to="/main/login">로그인</LoginItem>
      )}
      <Search />
    </Wrapper>
  );
};

export default TopBar;

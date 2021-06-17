import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import styled, { css, ThemeContext } from "styled-components";
import { Search } from "../../components";
import { EyeFilled, LoginOutlined } from "@ant-design/icons";
import { MenuItems } from "../../containers/MenuItems";
import TextField from "@material-ui/core/TextField";
import Autocomplete from "@material-ui/lab/Autocomplete";
import stocklist from "../../containers/AntennaTest/stocklist.json";
import "../../Fonts/index.css";

const withPathName = (Component) => (props) => {
  const history = useHistory();
  return <Component {...props} path={history.location.pathname} />;
};

const Logo = styled.div`
  height: 50px;
  font-family: "a아시아헤드3";
  font-size: 30px;
  font-weight: bold;
  padding: 0px 20px;
  cursor: pointer;
  color: #222831;
`;

const Wrapper = styled.div`
  background-color: #6363635d;
  padding-right: 10px;
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
  font-family: "a아시아헤드2";
  font-size: 22px;
  font-weight: 600;
  padding: 0px 16px;
  text-decoration: none;
  color: #222831;
  line-height: 70px;
  height: 70px;
  display: inline-block;
  position: relative;
  ::after {
    position: absolute;
    bottom: 10px;
    left: 0px;
    height: 3px;
    width: 0px;
    background-color: #f05454;
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
  font-family: "a아시아헤드2";
  font-size: 22px;
  font-weight: 600;
  padding: 0px 16px;
  text-decoration: none;
  color: #222831;
  line-height: 70px;
  height: 70px;
  display: inline-block;
  position: relative;
  ::after {
    position: absolute;
    bottom: 10px;
    left: 0px;
    height: 3px;
    width: 0px;
    background-color: #f05454;
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
const SearchBar = () => {
  const history = useHistory();
  const [company, setCompany] = useState({});
  return (
    <Autocomplete
      id="searchStock"
      company={company}
      onChange={(e, newcompany) => {
        console.log("newcompany", newcompany);
        if (newcompany) {
          console.log("newcomappny", newcompany);
          history.push({
            pathname: `/main/infoThresh/stock?code=${newcompany.code}&name=${newcompany.company}`,
          });
        }
      }}
      options={stocklist}
      getOptionLabel={(option) => option.company}
      style={{ width: 160 }}
      renderInput={(params) => (
        <TextField {...params} label="" variant="outlined" />
      )}
    ></Autocomplete>
  );
};
const TopBar = (props) => {
  const logged = window.sessionStorage.getItem("logged");
  console.log("logged??", logged);

  const history = useHistory();

  return (
    <Wrapper>
      <Logo onClick={() => history.push("/main/home")}>I N V E S T O C K</Logo>
      <PrettyOfWhiteSpace />
      <div>
        <MenuItem to="/main/antenna" color="#f05454">
          Antenna
        </MenuItem>
        <MenuItem to="/main/news">뉴스</MenuItem>
        <MenuItem to="/main/infoThresh">투자정보</MenuItem>
        <MenuItem to="/main/backtest">백테스트</MenuItem>
        <MenuItem to="/main/antenna/test">주가예측</MenuItem>
        <MenuItem to="/main/interest">관심종목</MenuItem>
      </div>
      {logged === "true" ? (
        <LoginItem to="/main/myPage">로그아웃</LoginItem>
      ) : (
        <LoginItem to="/main/login">로그인</LoginItem>
      )}
      <SearchBar></SearchBar>
    </Wrapper>
  );
};

export default TopBar;

import React, { useContext } from "react";
import { Link, useHistory } from "react-router-dom";
import styled, { css, ThemeContext } from "styled-components";
import { MText } from "../../components";

const withPathName = (Component) => (props) => {
  const history = useHistory();
  return <Component {...props} path={history.location.pathname} />;
};

const MenuItem = withPathName(styled(Link)`
  font-size: 16px;
  font-weight: 600;
  padding: 0px 0px;
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
const ThirdBox = () => {
  const history = useHistory();
  const theme = useContext(ThemeContext);

  const Wrapper = styled.div`
    width: 100%;
    height: 100%;
    display: inline-block;
    align-items: baseline;
    vertical-align: middle;
    margin-top: 120px;
    text-align: right;
  `;
  return (
    <Wrapper>
      <MText color="black">지금 &nbsp;</MText>
      <MText color="red">안테나</MText>
      <MText color="black">의 추천은?</MText>
      <br />
      <MenuItem to="/main/backtest">자세히보기</MenuItem>
      <br />
    </Wrapper>
  );
};

export default ThirdBox;

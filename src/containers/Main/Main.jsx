import React from "react";
import styled from "styled-components";
import {
  InvestBox,
  ItemBox,
  KospiBox,
  MainBox,
  NewsBox,
} from "../../components";

const Main = (props) => {
  const Layout = styled.div`
    width: 100%;
    height: 100%;
  `;
  const Wrapper = styled.div`
    height: calc(100%);
    border: 1px red solid;
  `;

  return (
    <Layout>
      <MainBox></MainBox>
      <KospiBox></KospiBox>
      <ItemBox></ItemBox>
      <NewsBox></NewsBox>
      <InvestBox></InvestBox>
    </Layout>
  );
};

export default Main;

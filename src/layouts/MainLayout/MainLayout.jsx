import React, { useState, useEffect } from "react";
import styled from "styled-components";
import TopBar from "./TopBar";
import Store from "../../store/Store";

const Layout = styled.div`
  width: 100%;
  height: 100%;
  min-width: 960px;
  background-color: ${(props) => props.theme.primaryColor};
`;

const ContentsWrapper = styled.div`
  height: calc(100% - 80px);
  overflow: auto;
`;

const MainLayout = (props) => {
  const { children } = props;

  return (
    <Layout>
      <TopBar />
      <ContentsWrapper>{children}</ContentsWrapper>
    </Layout>
  );
};

export default MainLayout;

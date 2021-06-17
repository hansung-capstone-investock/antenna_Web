import React from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import { MainNews } from "../News";
import { LiveNews } from "../News";
import { NewsData } from "../News";
import { Divider } from "antd";
import { NewsApp } from "../../components";

//뉴스 탭 "/main/news"

const Wrapper = styled.div`
  display: -ms-inline-grid;
  width: 95%;
  padding: 10px 0px 0px 40px;
  display: inline-block;

  @media screen and (max-width: 1300px) {
    position: inherit;
    display: block;
    height: 600px;
    width: 90vw;
    margin: 0 0 0 0;
  }
`;

const NewsWrapper = styled.div`
  width: calc(100%);
  height: 300px;
  margin: 10px 10px 20px 0;
  background-color: white;
  overflow-y: scroll;
  border: 5px solid #30475e;
`;

const NewsList = (props) => {
  return (
    <Wrapper>
      <NewsWrapper>
        <NewsData setPreview={props.setPreview}></NewsData>
      </NewsWrapper>

      <NewsWrapper>
        <LiveNews setPreview={props.setPreview}></LiveNews>
      </NewsWrapper>
    </Wrapper>
  );
};

export default NewsList;

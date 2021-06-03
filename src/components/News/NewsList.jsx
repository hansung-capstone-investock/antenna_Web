import React from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import { MainNews } from "../News";
import { LiveNews } from "../News";
import { NewsData } from "../News";
import { NewsApp } from "../../components";

const Wrapper = styled.div`
  display: -ms-inline-grid;
  width: 62%;
  display: inline-block;
  vertical-align: middle;

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
  height: 235px;
  margin: 0 10px 30px 30px;
  border: 6px solid #7d7d7d;
  padding-left: 10px;
  padding-right: 10px;
  background-color: white;
  overflow-y: scroll;
`;

const NewsList = (props) => {
  return (
    <Wrapper>
      <NewsWrapper>
        <NewsData setPreview={props.setPreview}></NewsData>
      </NewsWrapper>
      <NewsWrapper>
        <LiveNews></LiveNews>
      </NewsWrapper>
    </Wrapper>
  );
};

export default NewsList;

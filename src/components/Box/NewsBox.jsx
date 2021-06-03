import React from "react";
import styled from "styled-components";

const Box = styled.div`
  position: absolute;
  top: 400px;
  left: 40%;
  margin: 0 5%;
  display: inline-block;
  height: 180px;
  width: 260px;
  padding: 10px;
  box-shadow: 5px 5px 5px 5px gray;

  @media screen and (max-width: 1100px) {
    position: inherit;
    display: block;
    height: 600px;
    width: 100%;
    margin: 0px;
  }
  @media screen and (max-height: 600px) {
    position: inherit;
    display: block;
    height: 600px;
    width: 100%;
    margin: 0px;
  }
`;

const data = [
  {
    title: "Ant Design Title 1",
    summary: "News1",
    img: "https://imgnews.pstatic.net/image/origin/215/2021/04/08/949658.jpg",
  },
  {
    title: "Ant Design Title 2",
    summary: "News2",
    img: "https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png",
  },
  {
    title: "Ant Design Title 3",
    summary: "News3",
    img: "https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png",
  },
  {
    title: "Ant Design Title 4",
    summary: "News4",
    img: "https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png",
  },
];

const NewsUl = styled.ul`
  font-size: 10px;
  font-weight: 400;
`;
const NewsLi = styled.li`
  font-size: 8px;
  font-weight: 200;
`;

const NewsBox = () => {
  return (
    <Box>
      <NewsUl>{data[0].title}</NewsUl>
      <NewsLi>{data[0].summary}</NewsLi>
      <NewsUl>{data[1].title}</NewsUl>
      <NewsLi>{data[1].summary}</NewsLi>
      <NewsUl>{data[2].title}</NewsUl>
      <NewsLi>{data[2].summary}</NewsLi>
    </Box>
  );
};

export default NewsBox;

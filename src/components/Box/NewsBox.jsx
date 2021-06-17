import React from "react";
import styled from "styled-components";
import NewsforMain from "../News/NewsforMain";
import NewsData from "../News/NewsData";

const Box = styled.div`
  height: 100%;
  width: 100%;
  padding: 12% 5px 80px 15%;
`;

const NewsBox = () => {
  return (
    <Box>
      <NewsforMain />
    </Box>
  );
};

export default NewsBox;

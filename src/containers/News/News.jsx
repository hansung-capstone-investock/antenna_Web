import React, { useState } from "react";
import { NewsList } from "../../components";
import { Drawer } from "antd";
import styled from "styled-components";

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  vertical-align: middle;
  background-color: #f05454;
  display: flex;
`;

const News = (props) => {
  const [preview, setPreview] = useState();

  return (
    <Wrapper>
      <NewsList setPreview={setPreview}></NewsList>

      <Drawer
        width="80%"
        placement="right"
        visible={preview}
        onClose={() => {
          setPreview("");
        }}
      >
        <iframe
          style={{ width: "100%", height: "100%" }}
          src={preview}
        ></iframe>
      </Drawer>
    </Wrapper>
  );
};

export default News;

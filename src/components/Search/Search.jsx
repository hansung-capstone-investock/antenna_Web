import React from "react";
import styled from "styled-components";
import { SearchOutlined } from "@ant-design/icons";

const Wrapper = styled.div`
  height: 32px;
  font-size: 20px;
  color: ${(props) => props.theme.fontColor};
  line-height: 32px;
`;

const Input = styled.input.attrs({
  type: "text",
})`
  min-width: 32px;
  width: ${(props) => props.width || "100px"};
  height: 32px;
  padding: 0px 8px;
  background-color: rgba(0, 0, 0, 0);
  border: 0px !important;
  border-bottom: 1px solid ${(props) => props.theme.fontColor}!important;
  margin-right: 8px;
`;

const Icon = styled(SearchOutlined)`
  cursor: pointer;
`;

const Search = (props) => {
  return (
    <Wrapper>
      <Input width={props.width} />
      <Icon />
    </Wrapper>
  );
};

export default Search;

import React from "react";
import styled from "styled-components";

const MText = styled.div`
  float: ${(props) => props.float || "none"};
  margin-right: ${(props) => props.mright || "0"};
  margin: ${(props) => props.margin || "0 0 0 0"};
  display: ${(props) => props.display || "inline-block"};
  font-family: ${(props) => props.font || "a아시아헤드2"};
  font-size: ${(props) => props.size || "16px"};
  font-weight: ${(props) => props.weight || "600"};
  line-height: 1.59;
  text-shadow: ${(props) => props.shadow || ""};
  color: ${(props) => props.color || "#3b3b46"};
  align-items: ${(props) => props.alitem || "center"};
  padding-bottom: ${(props) => props.padBot || "5px"};
  padding: ${(props) => props.padding || ""};
  vertical-align: ${(props) => props.align || "middle"};
  text-shadow: 0 0 50px rgba(0, 0, 0, 0.18);
  position: ${(props) => props.position || "inherit"};
  top: ${(props) => props.top || "0"};
  left: ${(props) => props.left || "0"};
  background-color: ${(props) => props.bgcolor || ""};

  @media screen and (max-width: 1300px) {
    display: ${(props) => props.mediaDisplay || "inline-block"};
  }
`;

export default MText;

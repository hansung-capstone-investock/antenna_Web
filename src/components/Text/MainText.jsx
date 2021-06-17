import React from "react";
import styled from "styled-components";

const MainText = styled.div`
  font-family: ${(props) => props.font || "a아시아헤드2"};
  float: ${(props) => props.float || "none"};
  display: ${(props) => props.display || "block"};
  font-size: ${(props) => props.fontsize || "62px"};
  font-weight: 700;
  line-height: 1.3125;
  text-shadow: ${(props) => props.shadow || ""};
  color: ${(props) => props.color || "#f05454"};
  position: ${(props) => props.position || "inherit"};
  top: ${(props) => props.top || "0"};
  left: ${(props) => props.left || "0"};
  align-items: center;
  text-align: ${(props) => props.textalign || "left"};
  vertical-align: middle;
  text-shadow: 0 0 50px rgba(0, 0, 0, 0.163);
`;

export default MainText;

import React from "react";
import styled from "styled-components";

const MText = styled.div`
  float: ${(props) => props.float || "none"};
  margin-right: ${(props) => props.mright || "0"};
  display: inline-block;
  font-size: ${(props) => props.size || "16px"};
  font-weight: 550;
  line-height: 1.59;
  color: ${(props) => props.color || "#3b3b46"};
  align-items: center;
  padding-bottom: 5px;
  vertical-align: ${(props) => props.align || "middle"};
  text-shadow: 0 0 50px rgba(0, 0, 0, 0.18);
  position: ${(props) => props.position || "inherit"};
  top: ${(props) => props.top || "0"};
  left: ${(props) => props.left || "0"};

  @media screen and (max-width: 1300px) {
    display: ${(props) => props.mediaDisplay || "inline-block"};
  }
`;

export default MText;

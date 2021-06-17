import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { ChartKospi, KospiInfo } from "../../components";
import { MainText } from "../../components";
import { MText } from "../../components";
import axios from "axios";

const Box = styled.div`
  height: 100%;
  width: 100%;
  padding: 12% 5px 80px 15%;
`;
const KospiBox = () => {
  const [Kospi, setKospi] = useState([]);

  return (
    <Box>
      <KospiInfo text={true}></KospiInfo>
    </Box>
  );
};

export default KospiBox;

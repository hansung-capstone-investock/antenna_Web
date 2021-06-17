import {
  ChartKospi,
  KospiInfo,
  KospiData,
  MText,
  InfoTops,
} from "../../components";
import styled from "styled-components";
import React, { useState, useEffect, useHistory } from "react";
import queryString from "query-string";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  ReferenceLine,
} from "recharts";
import { Table, Tag, Space } from "antd";
/**
 * 투자정보 전체 페이지
 * @returns
 */
const InfoStock = () => {
  const Wrapper = styled.div`
    height: 100%;
    width: 100%;
    padding: 20px;
    display: inline-flex;

    .ant-table-wrapper {
      height: 400px;
    }
    .ant-table-cell {
      padding: 4px;
      height: 17px;
    }
  `;
  const BoxWrapper = styled.div`
    height: 80%;
    width: 50%;
  `;

  return (
    <div>
      <Wrapper>
        <BoxWrapper>
          <KospiInfo text={false} chartH="400px" chartW="600px" />
        </BoxWrapper>
        <BoxWrapper>
          <InfoTops></InfoTops>
        </BoxWrapper>
      </Wrapper>
    </div>
  );
};

export default InfoStock;

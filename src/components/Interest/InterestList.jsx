import React, { useState } from "react";
import styled from "styled-components";
import { Row, Col, Divider } from "antd";
import { DoIntBox, IntBox } from "../Interest";

/**
 * 관심종목 리스트 컴포넌트
 */

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  padding-top: 20px;
  background-color: #ebebebef;

  .ant-row {
    height: 500px;
  }
`;

const GroupWrapper = styled.div`
  width: 100%;
  height: 85%;
`;

const DivideCol = styled(Divider)`
  height: 100%;
  width: 1px;
`;

const InterestList = () => {
  return (
    <Wrapper>
      <Row justify="end">
        <Col flex="300px">
          <GroupWrapper>
            <DoIntBox />
          </GroupWrapper>
        </Col>
        <DivideCol type="vertical" />
        <Col flex="auto">
          <GroupWrapper>
            <IntBox i={0} />
          </GroupWrapper>
        </Col>
        <DivideCol type="vertical" />
        <Col flex="auto">
          <GroupWrapper>
            <IntBox i={1} />
          </GroupWrapper>
        </Col>
        <DivideCol type="vertical" />
        <Col flex="auto">
          <GroupWrapper>
            <IntBox i={2} />
          </GroupWrapper>
        </Col>
      </Row>
    </Wrapper>
  );
};
export default InterestList;

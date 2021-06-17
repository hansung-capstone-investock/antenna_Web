import React from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import { MainText } from "../../components";
import { MText } from "../../components";
import { AntBox, FirstBox, SecondBox } from "../../components";
import { Row, Col, Divider } from "antd";
import { GoAntTest } from "../../components";

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  padding: 0 10px 10px 30px;
`;
const GroupWrapper = styled.div`
  width: 100%;
  height: 100%;
`;
const Ant = () => {
  return (
    <Wrapper>
      <Row justify="end">
        <Col flex="500px">
          <GroupWrapper>
            <AntBox />
          </GroupWrapper>
        </Col>
        <Col flex="auto">
          <GroupWrapper>
            <FirstBox />
          </GroupWrapper>
        </Col>
        <Col flex="auto">
          <GroupWrapper>
            <SecondBox />
          </GroupWrapper>
        </Col>
      </Row>
    </Wrapper>
  );
};

export default Ant;

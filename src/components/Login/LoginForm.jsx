import { Form, Input, Button, Alert } from "antd";
import React, { useState } from "react";
import styled from "styled-components";
import { NewsData } from "../../components";
import { Route, Link, useHistory } from "react-router-dom";
import { MainText } from "../../components";
import { Logining } from "../../components";

const layout = {
  labelCol: { span: 10 },
  wrapperCol: { span: 6 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

const Wrapper = styled.div`
  padding: 100px;
  vertical-align: middle;
  align-items: center;
  width: 100%;
`;

const formWrapper = styled.div`
  width: 600px;
  vertical-align: middle;
  position: absolute;
  left: 10%;
  top: 15%;
`;

const LoginForm = (props) => {
  const [id, setid] = useState();
  const [pw, setpw] = useState();
  const [failed, setfailed] = useState();
  const history = useHistory();

  const msg = props.alert;

  //로그인 버튼 클릭 시
  const onFinish = (values: any) => {
    setid(values.id);
    setpw(values.pw);

    //로그인 함수 실행 후
    if (Logining(values)) {
      //성공하면 페이지 이동(새로고침)
    } else {
      //실패하면 페이지 이동(새로고침x 돌아가기)
      onFinishFailed();
      history.push("/main/login");
    }
  };

  const onFinishFailed = (errorInfo: any) => {
    setfailed("failed");
    console.log("Failed:", errorInfo);
  };

  return (
    <Wrapper>
      <formWrapper>
        <MainText color="black" textalign="center" fontsize="36px">
          Investock 로그인
        </MainText>
        <br />
        <Form
          {...layout}
          name="basic"
          initialValues={{ remember: true }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
        >
          {failed === "failed" ? (
            <Form.Item label=" ">
              <Alert message="로그인에 실패하였습니다." type="error" showIcon />
            </Form.Item>
          ) : (
            <div></div>
          )}
          {failed === "failed" ? (
            <Form.Item label=" ">
              <Alert message="로그인에 실패하였습니다." type="error" showIcon />
            </Form.Item>
          ) : (
            <div></div>
          )}
          {msg ? (
            <Form.Item label=" ">
              <Alert message={msg} type="error" showIcon />
            </Form.Item>
          ) : (
            <div></div>
          )}
          <Form.Item
            label="ID"
            name="id"
            rules={[{ required: true, message: "*" }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="pw"
            rules={[{ required: true, message: "*" }]}
          >
            <Input.Password />
          </Form.Item>
          <Form.Item
            {...tailLayout}
            wrapperCol={{ ...layout.wrapperCol, offset: 10 }}
          >
            <Button type="primary" htmlType="submit">
              로그인
            </Button>
            &nbsp;&nbsp;&nbsp;
            <Link to="/main/signUp">회원가입</Link>
          </Form.Item>
        </Form>
      </formWrapper>
    </Wrapper>
  );
};

export default LoginForm;

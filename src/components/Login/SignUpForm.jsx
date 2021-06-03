import { Form, Input, InputNumber, Button } from "antd";
import styled from "styled-components";
import { MainText, Signing } from "../../components";

const layout = {
  labelCol: { span: 9 },
  wrapperCol: { span: 6 },
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

/* eslint-disable no-template-curly-in-string */
const validateMessages = {
  required: "${label} is required!",
  types: {
    email: "${label} is not a valid email!",
    number: "${label} is not a valid number!",
  },
  number: {
    range: "${label} must be between ${min} and ${max}",
  },
};
/* eslint-enable no-template-curly-in-string */

const SignUpForm = () => {
  const onFinish = (values: any) => {
    console.log("before Signing");
    Signing(values);
  };

  return (
    <Wrapper>
      <formWrapper>
        <MainText color="black" textalign="center" fontsize="36px">
          Investock 회원가입
        </MainText>
        <br />
        <Form
          {...layout}
          name="nest-messages"
          onFinish={onFinish}
          validateMessages={validateMessages}
        >
          <Form.Item
            name={["user", "id"]}
            label="ID"
            rules={[{ required: true }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name={["user", "pw"]}
            label="PW"
            rules={[{ required: true }]}
          >
            <Input />
          </Form.Item>
          <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 9 }}>
            <Button type="primary" htmlType="submit">
              가입하기
            </Button>
          </Form.Item>
        </Form>
      </formWrapper>
    </Wrapper>
  );
};

export default SignUpForm;

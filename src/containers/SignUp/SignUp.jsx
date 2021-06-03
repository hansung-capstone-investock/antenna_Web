import styled from "styled-components";
import { SignUpForm } from "../../components";

const Wrapper = styled.div`
  vertical-align: middle;
  align-items: center;
  width: 100%;
  height: 100%;
`;

const Login = () => {
  return (
    <Wrapper>
      <SignUpForm></SignUpForm>
    </Wrapper>
  );
};

export default Login;

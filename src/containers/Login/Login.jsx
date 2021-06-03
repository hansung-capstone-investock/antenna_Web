import styled from "styled-components";
import { LoginForm } from "../../components";

const Wrapper = styled.div`
  vertical-align: middle;
  align-items: center;
  width: 100%;
  height: 100%;
`;

const Login = (props) => {
  console.log("값 넘어오는지", props.alert);

  return (
    <Wrapper>
      <LoginForm alert={props.alert}></LoginForm>
    </Wrapper>
  );
};

export default Login;

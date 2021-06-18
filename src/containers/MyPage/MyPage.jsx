import styled from "styled-components";
import { Form, Input, Button, Popconfirm, message } from "antd";
import { Route, Link, useHistory } from "react-router-dom";

const MyPage = () => {
  const history = useHistory();
  const doLogout = () => {
    const user = window.sessionStorage.getItem("id");
    console.log("logout합니다 >>> ", user);
    const conf = window.confirm("로그아웃 하시겠습니까?");
    if (conf) {
      window.sessionStorage.removeItem("id");
      window.sessionStorage.removeItem("pw");
      window.sessionStorage.setItem("logged", "false");
      //로그아웃 후 페이지 이동(새로고침)
      document.location.href = "/main/antenna";
    } else {
      history.push("/main/myPage");
    }
  };

  const confirm = () => {
    window.sessionStorage.removeItem("id");
    window.sessionStorage.removeItem("pw");
    window.sessionStorage.setItem("logged", "false");
    //로그아웃 후 페이지 이동(새로고침)
    document.location.href = "/main/antenna";
  };

  const cancel = () => {
    history.push("/main/myPage");
  };

  return (
    <div>
      <Popconfirm
        title="로그아웃하시겠습니까?"
        onConfirm={confirm}
        onCancel={cancel}
        okText="Yes"
        cancelText="No"
      >
        <Button>로그아웃</Button>
      </Popconfirm>
    </div>
  );
};

export default MyPage;

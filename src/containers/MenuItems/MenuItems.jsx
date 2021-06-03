import { Menu, Dropdown } from "antd";
import { MenuOutlined } from "@ant-design/icons";
import { Route, Link } from "react-router-dom";
import { menu } from "../MenuItems";
import styled from "styled-components";

const MenuItems = () => {
  const Wrapper = styled.div`
    display: none;
    @media screen and (max-width: 1100px) {
      display: flex;
    }
  `;

  const Drop = styled.a`
    text-decoration: none;
    color: black;
  `;
  return (
    <Wrapper>
      <Dropdown overlay={menu}>
        <a className="ant-dropdown-link" onClick={(e) => e.preventDefault()}>
          <MenuOutlined style={{ fontSize: "20px", color: "black" }} />
        </a>
      </Dropdown>
    </Wrapper>
  );
};

export default MenuItems;

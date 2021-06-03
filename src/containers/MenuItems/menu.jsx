import { Menu, Dropdown } from "antd";
import { DownOutlined } from "@ant-design/icons";
import { Route, Link } from "react-router-dom";

const menu = () => {
  return (
    <div>
      <Menu>
        <Menu.Item>
          <Link to="/main/antenna">Antenna</Link>
        </Menu.Item>
        <Menu.Item>
          <Link to="/main/news">뉴스</Link>
        </Menu.Item>
        <Menu.Item>
          <Link to="/main/intoThresh">투자정보</Link>
        </Menu.Item>
        <Menu.Item>
          <Link to="/main/backtest">백테스트</Link>
        </Menu.Item>
      </Menu>
    </div>
  );
};

export default menu;

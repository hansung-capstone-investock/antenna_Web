import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { Link, useHistory } from "react-router-dom";
import ReactDOM from "react-dom";
import axios from "axios";
import { Tabs } from "antd";
import { MText } from "../../components";
import { Table, Tag, Space } from "antd";
import {
  MinusCircleOutlined,
  LineOutlined,
  PlusCircleOutlined,
  GroupOutlined,
} from "@ant-design/icons";
import { Menu, Dropdown } from "antd";

const { TabPane } = Tabs;

const Wrapper = styled.div`
  width: 100%;
  height: 350px;
  padding: 10px 15px;
  border: 2px solid #dddddd;

  div.ant-table-header > table > thead > tr > th {
    background-color: white;
    font-family: "a고딕13";
    color: #808080;
  }
  .ant-tabs-tab-btn {
    font-family: "a고딕13";
    color: black;
  }
`;

const InfoTops = () => {
  const [Data, setData] = useState();
  const [Date, setDate] = useState();
  const [Price, setPrice] = useState();
  const [PriceTable, setPriceTable] = useState();
  const [Cap, setCap] = useState();
  const [CapTable, setCapTable] = useState();

  //관심종목 관련 데이터
  const [Int, setInt] = useState([]);
  const [Group, setGroup] = useState({});
  const [disable, setDisable] = useState([false, false, false]);

  async function GetInt() {
    await axios
      .post(
        "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/account/api/intereststockWeb/",
        {
          name: window.sessionStorage.getItem("id"),
        }
      )
      .catch(function (error) {
        console.log(error);
      })
      .then((response) => {
        if (response) {
          console.log("관심종목==> ", response.data);
          setGroup(response.data);
          response.data.map((r, idx) => {
            if (r.group == "") {
              r.group = "그룹" + idx;
            }
            var i = 0;
            for (var key in response.data[idx].companies) {
              if (response.data[idx].companies.key == "") {
                i++;
              }
            }
            if (i == 0) {
              if (idx == 0) {
                setDisable(true, disable[1], disable[2]);
              } else if (idx == 1) {
                setDisable(disable[0], true, disable[2]);
              } else {
                setDisable(disable[0], disable[1], true);
              }
            }
          });
        }
      });
  }
  async function GetInfoTops(code) {
    const response = await axios.get(
      "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/stock/topstock/"
    );
    if (response.data) {
      console.log("투자정보", response.data);
      setDate(response.data.date);
      setPrice(response.data.price);
      setCap(response.data.cap);
      setData(response.data);
    }
  }
  const [menu, setMenu] = useState(<Menu></Menu>);
  //추가할 종목 이름 저장 State
  const [StockName, setStockName] = useState("");
  const [GroupKey, setGroupKey] = useState();
  useEffect(() => {
    GetInt();
    GetInfoTops();
  }, []);

  useEffect(
    (props) => {
      if (Group.length > 0) {
        console.log("group", Group);
        setMenu(
          <Menu onClick={({ key }) => setGroupKey(key)}>
            <Menu.ItemGroup title="나의 그룹">
              <Menu.Item key="0" disabled={disable[0]}>
                {Group[0].group}
              </Menu.Item>
              <Menu.Item key="1" disabled={disable[1]}>
                {Group[1].group}
              </Menu.Item>
              <Menu.Item key="2" disabled={disable[2]}>
                {Group[2].group}
              </Menu.Item>
            </Menu.ItemGroup>
          </Menu>
        );
      }
    },
    [Group]
  );
  useEffect(() => {
    console.log("stockname groupkey변경됨", StockName, GroupKey);
    if (StockName && GroupKey) {
      AddInt(StockName, GroupKey);
    }
  }, [StockName, GroupKey]);
  //관심종목 추가 버튼 클릭 시
  const AddInt = (stname, props) => {
    console.log("props", stname, props);
    console.log("Group", Group);
    console.log("StockName", StockName);
    if (Group && StockName.length > 0) {
      const arr = ["", "", "", "", "", "", "", "", "", ""];
      var i = 0;
      for (var key in Group[props].companies) {
        if (Group[props].companies[key] != "") {
          arr[i] = Group[props].companies[key].company;
          i++;
        }
      }
      arr[i] = StockName;
      const PostData = {
        id: Group[props].id,
        name: window.sessionStorage.getItem("id"),
        group: Group[props].group,
        company1: arr[0],
        company2: arr[1],
        company3: arr[2],
        company4: arr[3],
        company5: arr[4],
        company6: arr[5],
        company7: arr[6],
        company8: arr[7],
        company9: arr[8],
        company10: arr[9],
      };
      console.log("postData?", PostData);

      axios
        .post(
          "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/account/api/interestUpdate/",
          PostData,
          { headers: { "Content-Type": "application/json" } }
        )
        .catch(function (error) {
          console.log(error);
        })
        .then((response) => {
          if (response) {
            console.log("업데이트되었나요? ", response);
          }
        });
    }

    setGroupKey();
    setStockName("");
  };
  useState(() => {}, [StockName]);

  //테이블 그리기
  const table = (data) => {
    const MyLink = styled(Link)`
      text-decoration: none;
      color: black;
    `;

    const FindCode = (text) => {
      var Code = "";
      Price.map((p, idx) => {
        if (p.company == text) {
          Code = p.stockcode;
        }
      });
      Cap.map((c, idx) => {
        if (c.company == text) {
          Code = c.stockcode;
        }
      });
      if (!Code) {
        Code = "error";
      }
      return Code;
    };

    if (data) {
      data.map((d, idx) => {
        if (String(d.diff).split(".").length > 1) {
          var before = String(d.diff).split(".");
          d.diff = before[0] + "." + before[1].substring(0, 2);
        }
      });
    }
    const col = [
      {
        title: "순위",
        dataIndex: "rank",
        width: "10%",
        render: (text) =>
          text == 1 ? (
            <MText font="a고딕15" size="15px" color="#0ca22a">
              &nbsp;{text}&nbsp;
            </MText>
          ) : (
            <MText font="a고딕15" size="13px" color="black">
              &nbsp;{text}&nbsp;
            </MText>
          ),
      },
      {
        title: "종목명",
        dataIndex: "company",
        width: "30%",
        render: (text, i) => (
          <MText font="a고딕11" size="12px">
            <MyLink
              to={`/main/infoThresh/stock?code=${FindCode(text)}&name=${text}`}
            >
              {text}
            </MyLink>
          </MText>
        ),
      },
      {
        title: "현재가",
        dataIndex: "todayPrice",
        render: (text) => (
          <MText font="a고딕13" size="11px">
            {text}
          </MText>
        ),
      },
      {
        title: "전일비",
        dataIndex: "diff",
        render: (text) =>
          text < 0 ? (
            <MText font="a고딕13" size="11px" color="blue">
              ▼&nbsp;{text}&nbsp;%
            </MText>
          ) : (
            <MText font="a고딕13" size="11px" color="red">
              ▲&nbsp;{text}&nbsp;%
            </MText>
          ),
      },
      {
        title: "",
        dataIndex: "company",
        width: "5%",
        render: (text) => (
          <Dropdown overlay={menu} trigger={["click"]} text={text}>
            <MText
              font="a고딕13"
              size="13px"
              color="#098021"
              padding="2px 0 0 0"
            >
              <PlusCircleOutlined onClick={() => setStockName(text)} />
            </MText>
          </Dropdown>
        ),
      },
    ];
    return (
      <Table
        className="table-striped-rows"
        dataSource={data}
        columns={col}
        scroll={{ x: 0, y: 500 }}
        pagination={false}
      />
    );
  };
  useEffect(() => {
    setPriceTable(table(Price));
    setCapTable(table(Cap));
  }, [Data]);

  const OnChange = (props) => {
    console.log("onchange", props);
  };

  return (
    <Wrapper>
      <MText font="a아시아헤드2" size="20px" color="red">
        Top
        <MText color="black" padding="3px 0 0 0">
          &nbsp;종목
        </MText>
      </MText>
      <Tabs
        onChange={OnChange}
        type="card"
        animated={{ inkBar: true, tabPane: false }}
      >
        <TabPane tab="상한가" key="1">
          {PriceTable}
        </TabPane>
        <TabPane tab="거래량 상위" key="2">
          {CapTable}
        </TabPane>
      </Tabs>
    </Wrapper>
  );
};

export default InfoTops;

import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { MainText, MText } from "../../components";
import axios from "axios";
import GetInt from "./GetInt";
import { List, Typography, Divider } from "antd";
import { Link, useHistory } from "react-router-dom";
import {
  MinusCircleOutlined,
  LineOutlined,
  PlusCircleOutlined,
} from "@ant-design/icons";
import { AutoComplete } from "antd";
import stocklist from "./stocklist.json";

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  padding: 60px 10px 10px 10px;
  display: block;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  .ant-list-bordered {
    border: 0;
  }
  .ant-list-split .ant-list-item {
    border: 0;
  }
`;

const StockLink = styled(Link)`
  text-decoration: none;
  color: #4f4f4f;
`;

const IntBox = (i) => {
  const [Group, setGroup] = useState([]);
  const [g, setG] = useState([]);
  const [data, setData] = useState({});
  const path = useHistory();
  console.log("name", window.sessionStorage.getItem("id"));
  useEffect(() => {
    axios
      .post(
        "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/account/api/intereststockWeb/",
        {
          name: window.sessionStorage.getItem("id"),
        },
        { headers: { "Content-Type": "application/json" } }
      )
      .catch(function (error) {
        console.log(error);
      })
      .then((response) => {
        if (response) {
          console.log("관심종목==> ", response.data);

          const cmps = response.data[i.i].companies;
          const c = [];
          for (var key in cmps) {
            c.push(cmps[key]);
          }
          setG(c);
          setGroup(response.data[i.i]);
        }
      });
  }, []);

  const UpdateInt = (props) => {
    console.log("props?", props);
    const arr = ["", "", "", "", "", "", "", "", "", ""];
    g.map((data, key) => {
      arr[key] = data.company;
      if (key == g.length - 1 && props) {
        arr[key + 1] = props;
      }
    });
    const PostData = {
      id: Group.id,
      name: window.sessionStorage.getItem("id"),
      group: Group.group,
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
    console.log("PostData", PostData);
    UpdatePosting(PostData);
  };

  const UpdatePosting = (PostData) => {
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
          //window.location.reload();
        }
      });
  };

  useEffect(() => {
    console.log("g", g);
  }, [g]);
  const [SBox, setSBox] = useState(false);
  const Complete = () => {
    const ComWrapper = styled.div`
      margin-right: 5px;
      float: right;
    `;
    const options = [];
    stocklist.map((stock, key) => {
      options.push({ value: stock.company, label: stock.company });
    });
    return (
      <ComWrapper>
        <AutoComplete
          style={{ width: 130 }}
          options={options}
          placeholder="이름으로 찾기"
          onChange={(val) => UpdateInt(val)}
        />
      </ComWrapper>
    );
  };

  const DeleteInt = (company) => {
    console.log("delete props", company);
    setG(g.filter((g) => g.company != company));
    console.log("deleted g?", g);
    const posting = g.filter((g) => g.company != company);
    const arr = ["", "", "", "", "", "", "", "", "", ""];
    posting.map((data, key) => {
      arr[key] = data.company;
    });
    console.log("Arr", arr);
    const PostData = {
      id: Group.id,
      name: window.sessionStorage.getItem("id"),
      group: Group.group,
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
    console.log("PostData", PostData);
    UpdatePosting(PostData);
  };

  return (
    <Wrapper>
      <MText
        color="#F05454"
        font="a고딕15"
        size="20px"
        margin="0px 0px 5px 5px"
      >
        그룹 {i.i + 1}
      </MText>
      <List
        className="fadeInLeft animated"
        size="small"
        header={
          <div>
            <MText color="#30475E" font="a고딕15" size="20px">
              {Group.group}
            </MText>
            <MText
              color="#247e05"
              font="a고딕11"
              size="18px"
              float="right"
              margin="3px 0 0 0 "
            >
              <PlusCircleOutlined onClick={() => setSBox(true)} />
            </MText>
            {SBox ? <Complete /> : <div></div>}
          </div>
        }
        bordered
        dataSource={g}
        renderItem={(item, idx) => (
          <List.Item>
            <MText color="#1b287b">{idx + 1}</MText>
            &nbsp; &nbsp;
            <MText color="#4f4f4f" font="a고딕11">
              <StockLink
                to={`/main/infoThresh/stock?code=${item.code}&name=${item.company}`}
              >
                {item.company}
              </StockLink>
            </MText>
            <MText
              size="13px"
              color={item.diff < 0 ? "blue" : "red"}
              font="a고딕11"
              float="right"
            >
              {item.diff < 0 ? "▼" : "▲"}&nbsp;{item.diff}&nbsp;&nbsp;
              {item.diffrate}&nbsp;%&nbsp;&nbsp;
              <MText display="inline-flex" margin="4px 0 0 0" color="#ffa600">
                <MinusCircleOutlined onClick={() => DeleteInt(item.company)} />
              </MText>
            </MText>
          </List.Item>
        )}
      />
    </Wrapper>
  );
};

export default IntBox;

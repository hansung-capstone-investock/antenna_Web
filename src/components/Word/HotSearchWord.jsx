import React, { useState, useEffect } from "react";
import styled from "styled-components";
import ReactDOM from "react-dom";
import axios from "axios";
import { List, Divider } from "antd";
import { MText } from "../../components";

const HotSearchWord = () => {
  const Wrapper = styled.div`
    width: 100%;
    height: 100%auto;

    .ant-list-header {
      background-color: #fbfbfb;
      margin: 3px 7px 0 7px;
    }
    @media screen and (max-width: 1300px) {
      display: none;
    }
  `;

  const ItemWrapper = styled.div`
    margin: 1px;
    //뉴스 아이템 타이틀
    .ant-list-item-meta-title {
      padding: 0px 10px;
    }

    //뉴스 item 간 divider
    .ant-divider-horizontal {
      margin: 5px 0px;
      width: 80%;
    }
  `;
  const [dc, setDc] = useState([
    { order: "1", title: "" },
    { order: "2", title: "" },
    { order: "3", title: "" },
    { order: "4", title: "" },
    { order: "5", title: "" },
  ]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchHword = async () => {
      try {
        setError(null);
        setDc(null);
        setLoading(true);
        const response = await axios.get(
          "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/views/api/dcList",
          (req, res) => {
            req.header("Access-Control-Allow-Origin", "*");
            res.header("Access-Control-Allow-Origin", "*");
          }
        );
        const data = response.data;
        console.log("dc", response.data);
        setDc([
          { order: "1", title: data[0].title },
          { order: "2", title: data[1].title },
          { order: "3", title: data[2].title },
          { order: "4", title: data[3].title },
          { order: "5", title: data[4].title },
          { order: "6", title: data[5].title },
          { order: "7", title: data[6].title },
          { order: "8", title: data[7].title },
          { order: "9", title: data[8].title },
          { order: "10", title: data[9].title },
        ]);
      } catch (e) {
        setError(e);
        console.log(error);
      }
      setLoading(false);
    };

    fetchHword();
  }, []);
  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다</div>;

  return (
    <Wrapper>
      <List
        header={
          <MText
            display="inline-flex"
            color="#222831"
            font="a아시아헤드3"
            padding="0px 0px 0px 10px"
          >
            <MText
              color="#f05454"
              font="a아시아헤드3"
              padding="0px 0px 0px 0px"
            >
              실시간
            </MText>{" "}
            &nbsp;키워드
          </MText>
        }
        itemLayout="horizontal"
        dataSource={dc}
        renderItem={(item) => (
          <ItemWrapper>
            <List.Item.Meta
              title={
                <MText
                  display="inline-flex"
                  color="#9b9b9b"
                  font="a아시아헤드1"
                  padding="0px 0px 0px 10px"
                  weight="300"
                  margin="3px 0 0 0"
                >
                  <MText
                    color="#0800e9"
                    font="a아시아헤드3"
                    padding="0px 0px 0px 0px"
                    weight="500"
                  >
                    {item.order}
                  </MText>
                  &nbsp;&nbsp;{item.title}
                </MText>
              }
            ></List.Item.Meta>
            <Divider />
          </ItemWrapper>
        )}
      ></List>
    </Wrapper>
  );
};

export default HotSearchWord;

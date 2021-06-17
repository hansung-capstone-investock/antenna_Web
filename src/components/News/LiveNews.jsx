import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import styled from "styled-components";
import { List, Divider } from "antd";
import { MText } from "../../components";

function LiveNews(props) {
  const ItemWrapper = styled.div`
    margin: 1px;
    //뉴스 아이템 타이틀
    .ant-list-item-meta-title {
      padding: 0px 10px;
    }
    //뉴스 아이템 세부설명
    .ant-list-item-meta-description {
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      font-family: "a아시아헤드1";
      padding-left: 15px;
    }
    //뉴스 item 간 divider
    .ant-divider-horizontal {
      margin: 3px 0px;
      width: 80%;
    }
  `;

  const Wrapper = styled.div`
    width: calc(100%);
    .ant-list-header {
      background-color: #dddddd;
      margin: 7px 7px 0 7px;
    }
  `;

  const [news, setNews] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        setError(null);
        setNews(null);
        setLoading(true);
        const response = await axios.get(
          "http://ec2-3-37-87-254.ap-northeast-2.compute.amazonaws.com:8000/views/api/livenews"
          // (req, res) => {
          //   req.header("Access-Control-Allow-Origin", "*");
          //   res.header("Access-Control-Allow-Origin", "*");
          // }
        );
        setNews(response.data); // 데이터는 response.data 안에 들어있습니다.
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };

    fetchNews();
  }, []);

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다</div>;
  if (!news) return null;

  const Anews = styled.a`
    font-family: "a아시아헤드3";
    color: #222831;
  `;

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
              TODAY
            </MText>{" "}
            &nbsp;실시간 뉴스
          </MText>
        }
        itemLayout="horizontal"
        dataSource={news}
        renderItem={(item) => (
          <ItemWrapper>
            <List.Item.Meta
              title={
                <Anews
                  onClick={(evt) => {
                    evt.preventDefault();
                    props.setPreview(item.link);
                  }}
                  href={item.link}
                >
                  {item.title}
                </Anews>
              }
              description={item.summary}
            ></List.Item.Meta>
            <Divider />
          </ItemWrapper>
        )}
      ></List>
    </Wrapper>
  );
}

export default LiveNews;

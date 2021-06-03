import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import styled from "styled-components";
import { List } from "antd";

function NewsData(props) {
  const ItemWrapper = styled.div`
    margin: 1px;
    .ant-list-item-meta-description {
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }
  `;

  const Wrapper = styled.div`
    width: calc(100%);
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
          "http://ec2-13-125-236-101.ap-northeast-2.compute.amazonaws.com:8000/views/api/news",
          (req, res) => {
            req.header("Access-Control-Allow-Origin", "*");
            res.header("Access-Control-Allow-Origin", "*");
          }
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

  return (
    <Wrapper>
      <List
        header={<div>메인뉴스</div>}
        itemLayout="horizontal"
        dataSource={news}
        renderItem={(item) => (
          <ItemWrapper>
            <List.Item.Meta
              title={
                <a
                  onClick={(evt) => {
                    evt.preventDefault();
                    props.setPreview(item.link);
                  }}
                  href={item.link}
                >
                  {item.title}
                </a>
              }
              description={item.summary}
            ></List.Item.Meta>
          </ItemWrapper>
        )}
      ></List>
    </Wrapper>
  );
}

export default NewsData;

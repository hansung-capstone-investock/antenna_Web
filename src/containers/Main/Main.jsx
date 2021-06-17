import React from "react";
import styled from "styled-components";
import {
  InvestBox,
  ItemBox,
  KospiBox,
  MainBox,
  NewsBox,
} from "../../components";
import { Carousel } from "antd";
import "./Main.css";

/**
 * "/main/home"
 */
const CarouselWrapper = styled(Carousel)`
  > .slick-dots li button {
    background: #afafaf;
  }
  > .slick-dots li.slick-active button {
    background: #f05454;
  }
`;
const Main = (props) => {
  const Layout = styled.div`
    padding: 20px;
    width: 100%;
    height: 100%;
    display: inline-flex;
  `;

  const Wrapper = styled.div`
    width: 50%;
    height: 600px;
  `;
  const contentStyle = {
    height: "500px",
    color: "#000000",
    lineHeight: "500px",
    textAlign: "center",
  };

  return (
    <Layout>
      <Wrapper>
        <MainBox />
      </Wrapper>
      <Wrapper>
        <CarouselWrapper autoplay={false} effect="fade">
          <div>
            <h3 style={contentStyle}>
              <KospiBox />
            </h3>
          </div>
          <div>
            <h3 style={contentStyle}>
              <NewsBox />
            </h3>
          </div>
          <div>
            <h3 style={contentStyle}>
              <ItemBox />
            </h3>
          </div>
        </CarouselWrapper>
      </Wrapper>
    </Layout>
  );
};

export default Main;

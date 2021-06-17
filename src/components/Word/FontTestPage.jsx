import "../../Fonts/index.css";
import react from "react";
import styled from "styled-components";

const text = "Investock, Antenna, 안녕하세요!! 입니다!! ~~~~ , 123456\n";

const fontlist = [
  "a고딕11",
  "a고딕13",
  "a고딕15",
  "a고딕17",
  "a아시아헤드1",
  "a아시아헤드2",
  "a아시아헤드3",
  "josefinB",
  "josefinL",
  "josefinR",
  "juliusR",
  "Mfont",
  "nanumRoundB",
  "nanumRoundL",
  "righteousR",
  "sixCapsR",
];

const FontBox = styled.div`
  font-family: ${(props) => props.font || ""};
  font-size: 20pt;
  border: 1px black solid;
`;

const FontTestPage = () => {
  const boxlist = [];
  fontlist.map((font) => {
    boxlist.push(<FontBox font={font}>{text}</FontBox>);
    console.log("boxlist", boxlist);
  });

  return <div>{boxlist}</div>;
};

export default FontTestPage;

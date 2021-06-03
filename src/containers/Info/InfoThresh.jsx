import { ChartKospi, KospiInfo, KospiData } from "../../components";
import styled from "styled-components";

const InfoThresh = () => {
  const Wrapper = styled.div`
    width: 400px;
    height: 600px;
  `;

  return (
    <div>
      <KospiInfo></KospiInfo>
    </div>
  );
};

export default InfoThresh;

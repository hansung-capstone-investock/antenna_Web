import React, { useState, useEffect, PureComponent } from "react";
import { Line } from "react-chartjs-2";
import { ResponsiveLine } from "nivo";
import axios from "axios";

const ChartKospi = () => {
  const [Kospi, setKospi] = useState({});
  useEffect(() => {
    const fetchKospi = async () => {
      const res = await axios.get(
        "http://ec2-13-125-236-101.ap-northeast-2.compute.amazonaws.com:8000/stock/kospiyear/",
        (req, res) => {
          req.header("Access-Control-Allow-Origin", "*");
          res.header("Access-Control-Allow-Origin", "*");
        }
      );
      makeData(res.data);
      console.log("res data", res.data);
    };

    const makeData = (items) => {
      const arr = items.reduce((acc, cur) => {
        const date = cur.date.substr(0, 10);
        const close = cur.close;

        acc.push({ date, close });
        return acc;
      }, []);

      const labels = arr.map((a) => `${a.date}`);
      setKospi({
        labels,
        datasets: [
          {
            label: "코스피 지수",
            backgroundColor: "rgba(255, 55, 55, 0.251)",
            borderColor: "red",
            fill: true,
            lineTension: 0.1,
            data: arr.map((a) => a.close),

            pointBorderColor: "red",
            pointBackgroundColor: "red",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "red",
            pointHoverBorderColor: "white",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
          },
        ],
      });
    };
    fetchKospi();
  }, []);

  return (
    <section>
      <div className="contents">
        <div>
          <Line
            height={1000}
            width={1500}
            data={Kospi}
            options={
              ({
                scales: {
                  xAxes: [
                    {
                      display: true,
                      scaleLabel: {
                        display: true,
                        labelString: "Step",
                        fontFamily: "Montserrat",
                        fontColor: "black",
                      },
                      ticks: {
                        maxTicksLimit: 12,
                        autoSkip: false, //레이블 자동 계산
                      },
                    },
                  ],
                  yAxes: [
                    {
                      ticks: {
                        maxTicksLimit: 12,
                      },
                    },
                  ],
                },
                maintainAspectRatio: false,
                titile: {
                  display: true,
                  text: "코스피지수",
                  fontsize: 16,
                },
              },
              {
                legend: {
                  display: true,
                  position: "bottom",
                },
              })
            }
          />
        </div>
      </div>
    </section>
  );
};

export default ChartKospi;

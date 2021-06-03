import { KospiData } from "../../components";
import axios from "axios";

class Chart {
  constructor(canvas) {
    this.ctx = canvas.getContext("2d");
    this.width = canvas.clientWidth;
    this.height = canvas.clientHeight;
    this.datas = [];
    window.requestAnimationFrame(this.drawAll);
  }

  drawAll = (now) => {
    const { ctx, width, height } = this;

    const etime = Date.now();
    const duration = 1000 * 60;
    const stime = etime - duration;
    const maxValue = 3500;

    ctx.clearRect(0, 0, width, height);
    ctx.beginPath();
    ctx.fillStyle = "red";
    this.datas.forEach((data, i) => {
      const [time, value] = data;

      const x = (width * (time - stime)) / duration;
      const y = height - (height * value) / maxValue;

      if (i) {
        ctx.lineTo(x, y);
        if (i === this.datas.length - 1) {
          ctx.lineTo(x, height);
        }
      } else {
        ctx.moveTo(x, height);
        ctx.lineTo(x, y);
      }
    });

    ctx.fill();

    window.requestAnimationFrame(this.drawAll);
  };

  addData = () => {
    const KospiDatas = KospiData();
    console.log("KospiData호출 in Chart", KospiDatas);
  };
}

export default Chart;

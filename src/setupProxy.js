const { createProxyMiddleware } = require("http-proxy-middleware");
module.exports = function (app) {
  app.use(
    "/views",
    createProxyMiddleware({
      target:
        "http://ec2-13-125-236-101.ap-northeast-2.compute.amazonaws.com:8000",
      changeOrigin: true,
    })
  );
};

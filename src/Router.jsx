import React, { useEffect } from "react";
import { BrowserRouter, Switch, Route, useHistory } from "react-router-dom";
import * as Layouts from "./layouts";
import * as Containers from "./containers";
import { withLivePanel } from "./hoc";

const News = withLivePanel(Containers.News);
const Antenna = withLivePanel(Containers.Antenna, true);

const RedirectMain = () => {
  const history = useHistory();
  useEffect(() => history.push("/main/home"));
  return <></>;
};

const Router = () => {
  const logged = window.sessionStorage.getItem("logged");
  console.log("logged??", logged);
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact>
          <RedirectMain />
        </Route>
        <Route
          path="/main"
          render={() => (
            <Layouts.MainLayout>
              <Route path="/main/home" exact>
                <Containers.Main />
              </Route>
              <Route path="/main/antenna">
                <Antenna />
              </Route>
              <Route path="/main/news">
                <News />
              </Route>
              <Route path="/main/infoThresh" exact>
                <Containers.InfoThresh />
              </Route>
              <Route path="/main/backtest">
                {logged === "true" ? (
                  <Containers.Backtest />
                ) : (
                  <Containers.Login alert="로그인이 필요합니다." />
                )}
              </Route>
              <Route path="/main/login">
                {logged === "true" ? (
                  <Containers.MyPage />
                ) : (
                  <Containers.Login />
                )}
              </Route>
              <Route path="/main/myPage">
                {logged === "true" ? (
                  <Containers.MyPage />
                ) : (
                  <Containers.Login alert="로그인이 필요합니다." />
                )}
              </Route>
              <Route path="/main/signUp">
                <Containers.SignUp />
              </Route>
            </Layouts.MainLayout>
          )}
        ></Route>
        <Route path="*">404</Route>
      </Switch>
    </BrowserRouter>
  );
};

export default Router;

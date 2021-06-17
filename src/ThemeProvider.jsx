import React, { useState, useCallback } from "react";
import { ThemeProvider as StyledThemeProvider } from "styled-components";

const whiteTheme = {
  theme: "wh",
  bgColor: "#FFFFFF",
  fontColor: "#000000",
  primaryColor: "#ffffff",
};

const darkTheme = {
  ...whiteTheme,
  theme: "bk",
  bgColor: "#000000",
  fontColor: "#FFFFFF",
  primaryColor: "#d3d3d3",
};

const ThemeProvider = (props) => {
  const { children } = props;
  const [theme, setTheme] = useState(whiteTheme);

  const changeTheme = useCallback(() => {
    if (theme === whiteTheme) {
      setTheme(darkTheme);
    } else {
      setTheme(whiteTheme);
    }
  }, [theme]);

  console.log("children?", children);
  return (
    <StyledThemeProvider theme={{ ...theme, changeTheme }}>
      {children}
    </StyledThemeProvider>
  );
};

export default ThemeProvider;

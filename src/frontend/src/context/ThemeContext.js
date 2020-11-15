import React, { useState } from "react";

export const ThemeContext = React.createContext({
	theme: "",
	toggleTheme: () => {},
});

export const ThemeContextProvider = (props) => {
	const [theme, toggleTheme] = useState("normal");
	return (
		<ThemeContext.Provider
			value={{
				theme,
				toggleTheme,
			}}>
			{props.children}
		</ThemeContext.Provider>
	);
};

import { Fragment } from "react";

import { routes } from "./routes";
import { RouterProvider } from "react-router-dom";
import { store } from "./store";
import { Provider } from "react-redux";
function App() {
  //https://tailwindcss.com/docs/installation/using-postcss
  //https://redux-toolkit.js.org/tutorials/quick-start
  return (
    <Fragment>
      <Provider store={store}>
        <RouterProvider router={routes} />
      </Provider>
    </Fragment>
  );
}

export default App;

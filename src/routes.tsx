import { createBrowserRouter } from "react-router-dom";

import Error from "./components/Error";
import Home from "./components/Home/Home";
import CreateTodo from "./components/Todo/CreateTodo";
import Todo from "./components/Todo/Todo";
import UpdateTodo from "./components/Todo/UpdateTodo";
import TodoLayout from "./components/Todo/TodoLayout";
export const routes = createBrowserRouter([
  {
    path: "/",
    errorElement: <Error />,
    element: <Home />,
  },
  {
    path: "todo",
    element: <TodoLayout />,
    children: [
      {
        index: true,
        element: <Todo />,
      },
      {
        path: "new",
        element: <CreateTodo />,
      },
      {
        path: ":id",
        element: <UpdateTodo />,
      },
    ],
  },
]);

import { Outlet } from "react-router-dom";
import Sidebar from "../Sidebar/Sidebar";

function TodoLayout() {
  return (
    <div>
      <Sidebar /> <Outlet />
    </div>
  );
}

export default TodoLayout;

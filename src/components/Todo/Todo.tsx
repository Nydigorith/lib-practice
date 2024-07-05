import { useAppSelector, useAppDispatch } from "../../hooks";
import { RootState } from "../../store";
import { decrement, incrementByAmount } from "../../slice/todoSlice";
function Todo() {
  const count = useAppSelector((state: RootState) => state.counter.value);
  const dispatch = useAppDispatch();

  return (
    <div>
      Todo
      <div>Count : {count}</div>
      <button
        onClick={() => {
          dispatch(decrement());
        }}
      >
        Decrement
      </button>
      <button
        onClick={() => {
          dispatch(incrementByAmount(2));
        }}
      >
        Increment by 2
      </button>
    </div>
  );
}

export default Todo;

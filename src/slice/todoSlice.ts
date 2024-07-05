import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface TodoState {
  value: number;
}

const initialState: TodoState = {
  value: 0,
};

export const todoSlice = createSlice({
  name: "todo",
  initialState,
  reducers: {
   
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const {decrement, incrementByAmount } = todoSlice.actions;

export default todoSlice.reducer;

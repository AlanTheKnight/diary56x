import { Module } from "vuex";
import { authState } from "./state";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";
import { DiaryState } from "./types";
import { RootState } from "@/store";

export const diary: Module<DiaryState, RootState> = {
  state: authState,
  getters,
  mutations,
  actions,
};

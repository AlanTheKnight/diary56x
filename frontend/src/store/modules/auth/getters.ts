import { RootState } from "@/store";
import { GetterTree } from "vuex";
import { AuthState, Getters } from "./types";

export const getters: GetterTree<AuthState, RootState> & Getters = {
  isAuthenticated: (state) =>
    Boolean(state.accessToken && state.refreshToken && state.user),
  messagesLength: (state) => state.messages.length,
  unreadNotificationsCount: (state) => state.unread_notifications.length,
};

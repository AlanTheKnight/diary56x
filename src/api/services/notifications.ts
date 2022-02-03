import API from "@/api";
import { AxiosResponse } from "axios";
import { Paginator } from "../types";

export interface PageParam {
  page?: number;
}

export enum NotificationAPIURLS {
  LIST = "notifications/",
  DETAIL = "notifications/",
  CREATE = "notifications/",
}

export interface APINotification {
  id: number;
  title: string;
  text: string;
  read: boolean;
  created_at: string;
  user: number;
}

export interface CreateNotification {
  title: string;
  text: string;
  user: number;
}

interface ListNotificationsParams extends PageParam {
  user?: number;
  read?: boolean;
}

export const listNotifications = (
  params: ListNotificationsParams
): Promise<AxiosResponse<Paginator<APINotification>>> => {
  return API.axios.get<Paginator<APINotification>>(NotificationAPIURLS.LIST, {
    params: params,
  });
};

export const retrieveNotification = (
  id: number
): Promise<AxiosResponse<APINotification>> => {
  return API.axios.get<APINotification>(NotificationAPIURLS.DETAIL + id);
};

export const createNotification = (
  data: CreateNotification
): Promise<AxiosResponse<APINotification>> => {
  return API.axios.post<APINotification>(NotificationAPIURLS.CREATE, data);
};

export const deleteNotification = (
  id: number
): Promise<AxiosResponse<APINotification>> => {
  return API.axios.delete<APINotification>(NotificationAPIURLS.DETAIL + id);
};

export const markNotificationAsRead = (
  id: number
): Promise<AxiosResponse<APINotification>> => {
  return API.axios.patch<APINotification>(
    NotificationAPIURLS.DETAIL + id + "/",
    {
      read: true,
    }
  );
};
import API from "@/api";
import { AxiosResponse } from "axios";

const SubjectsAPIEndpoint = "subjects/";

export interface APISubject {
  id: number;
  name: string;
  description: string;
  icon: string;
}

export const listSubjects = (
  params?: URLSearchParams
): Promise<AxiosResponse<APISubject[]>> => {
  return API.axios.get(SubjectsAPIEndpoint, {
    params,
  });
};

export const getSubject = (id: number): Promise<AxiosResponse<APISubject>> => {
  return API.axios.get(SubjectsAPIEndpoint + id + "/");
};

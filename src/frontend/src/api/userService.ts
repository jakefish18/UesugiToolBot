import apiClient from "@/api/apiClient";
import {UserProfile} from "@/types/user";

export const getUserProfile = async (): Promise<UserProfile> => {
    const response = await apiClient.get<UserProfile>("/users/me");
    return response.data;
}

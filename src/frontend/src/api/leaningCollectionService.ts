import apiClient from "@/api/apiClient";

export const getAllLearningCollections = async (): Promise<UserProfile> => {
    const response = await apiClient.get<UserProfile>("/users/me");
    return response.data;
}

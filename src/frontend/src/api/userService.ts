import apiClient from "@/api/apiClient";
import {UserProfile} from "@/types/user";
import {LearningCollectionPreview} from "@/types/learningCollection";

export const getUserProfile = async (): Promise<UserProfile> => {
    const response = await apiClient.get<UserProfile>("/users/me");
    return response.data;
}

export const getUserLearningCollections = async (): Promise<LearningCollectionPreview[]> => {
    const response = await apiClient.get<LearningCollectionPreview[]>("/users/me/learning_collections");
    return response.data;
}
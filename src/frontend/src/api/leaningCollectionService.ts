import apiClient from "@/api/apiClient";
import {LearningCollectionPreview} from "@/types/learningCollection";

export const getAllLearningCollections = async (): Promise<LearningCollectionPreview[]> => {
    const response = await apiClient.get<LearningCollectionPreview[]>("/learning_collections/all");
    return response.data;
}

export const postLearningCollection = async (learning_collection_id: number): Promise<number> => {
    const response = await apiClient.post(`/users/me/learning_collections/${learning_collection_id}`);
    return response.status
}
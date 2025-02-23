import apiClient from "@/api/apiClient";
import {LearningCollectionPreview} from "@/types/learningCollection";

export const getAllLearningCollections = async (): Promise<LearningCollectionPreview[]> => {
    const response = await apiClient.get<LearningCollectionPreview[]>("/learning_collections/all");
    return response.data;
}

export const searchLearningCollections = async (query: string, limit: bigint, offset: bigint): Promise<LearningCollectionPreview[]> => {
    const response = await apiClient.get<LearningCollectionPreview[]>("/learning_collections/search", {
        params: {
            query: query,
            limit: limit,
            offset: offset
        }
    });
    return response.data;
}

export const postLearningCollection = async (learning_collection_id: number): Promise<number> => {
    const response = await apiClient.post(`/users/me/learning_collections/${learning_collection_id}`);
    return response.status
}

export const deleteLearningCollection = async (learning_collection_id: number): Promise<number> => {
    const response = await apiClient.delete(`/users/me/learning_collections/${learning_collection_id}`);
    return response.status
}
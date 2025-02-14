import apiClient from "@/api/apiClient";
import {LearningCollectionPreview} from "@/types/learningCollection";

export const getAllLearningCollections = async (): Promise<LearningCollectionPreview[]> => {
    const response = await apiClient.get<LearningCollectionPreview[]>("/learning_collections/all");
    return response.data;
}

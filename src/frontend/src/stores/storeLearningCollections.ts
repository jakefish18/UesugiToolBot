import { defineStore } from "pinia";
import {LearningCollectionPreview} from "@/types/learningCollection";
import {getAllLearningCollections, searchLearningCollections} from "@/api/leaningCollectionService";

export const useLearningCollectionsStore = defineStore("learning_collection", {
    state: () => ({
        isLoaded: false,
        learningCollections: [] as LearningCollectionPreview[],
    }),

    actions: {
        async fetchLearningCollections() {
            try {
                this.isLoaded = false;
                this.learningCollections.length = 0;
                const response = await getAllLearningCollections();
                response.forEach((learningCollection) => {
                    this.learningCollections.push(learningCollection);
                })
                this.isLoaded = true;
            } catch (err) {
                console.log("Learning collections weren't fetched");
            }
        },
        async searchLearningCollection(query: string, limit: bigint, offset: bigint) {
            try {
                this.isLoaded = false;
                this.learningCollections.length = 0;
                const response = await searchLearningCollections(query, limit, offset);
                response.forEach((learningCollection) => {
                    this.learningCollections.push(learningCollection);
                })
                this.isLoaded = true;
            } catch (err) {
                console.log("Learning collections search was unsuccessfull");
            }
        },
        getById(learningCollectionId: bigint): LearningCollectionPreview {
            return this.learningCollections.find(learningCollection => learningCollection.id == learningCollectionId)!;
        }
    },
})
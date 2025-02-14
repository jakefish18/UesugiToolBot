import { defineStore } from "pinia";
import {LearningCollectionPreview} from "@/types/learningCollection";
import {getAllLearningCollections} from "@/api/leaningCollectionService";

export const useLearningCollectionsStore = defineStore("learning_collection", {
    state: () => ({
        isLoaded: false,
        learningCollections: [] as LearningCollectionPreview[],
    }),

    actions: {
        async fetchLearningCollections() {
            try {
                this.learningCollections.length = 0;
                const response = await getAllLearningCollections();
                response.forEach((learningCollection) => {
                    this.learningCollections.push(learningCollection);
                })
                this.isLoaded = true;
            } catch (err) {
                console.log("Learning collections weren't fetched");
            }
        }
    },
})
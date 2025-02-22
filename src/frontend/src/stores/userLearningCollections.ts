import { defineStore } from "pinia";
import {LearningCollectionPreview} from "@/types/learningCollection";
import { getUserLearningCollections } from "@/api/userService";
import {postLearningCollection} from "@/api/leaningCollectionService";

export const useUserLearningCollectionsStore = defineStore("user_learning_collection", {
    state: () => ({
        isLoaded: false,
        userLearningCollections: [] as LearningCollectionPreview[],
    }),

    actions: {
        async fetchUserLearningCollections() {
            try {
                this.userLearningCollections.length = 0;
                const response = await getUserLearningCollections();
                response.forEach((learningCollection) => {
                    this.userLearningCollections.push(learningCollection);
                })
                this.isLoaded = true;
            } catch (err) {
                console.log("Learning collections weren't fetched");
            }
        },

        deleteUserLearningCollection(learningCollectionToDeleteId: bigint) {
          this.userLearningCollections = this.userLearningCollections.filter(
              learningCollection => learningCollection.id != learningCollectionToDeleteId
          );
        },

        addUserLearningCollection(learningCollection: LearningCollectionPreview) {
            this.userLearningCollections.push(learningCollection);
        },

        isCollection(learningCollectionId: bigint): boolean {
            return this.userLearningCollections.some(i => i.id == learningCollectionId);
        }
    },
})
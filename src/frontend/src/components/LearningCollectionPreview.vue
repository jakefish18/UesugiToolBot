<script setup lang="ts">
import {LearningCollectionPreview} from "@/types/learningCollection";
import BlueButton from "@/components/BlueButton.vue";
import learningCollectionImage from "@/assets/default_learning_collection_image.png";
import {useUserLearningCollectionsStore} from "@/stores/userLearningCollections";
import {useLearningCollectionsStore} from "@/stores/storeLearningCollections";
import {postLearningCollection, deleteLearningCollection} from "@/api/leaningCollectionService";

const userLearningCollectionsStore = useUserLearningCollectionsStore();
const learningCollectionsStore = useLearningCollectionsStore();

const props =  defineProps<{
  id: bigint
  name: string
  ownerId: bigint
  numberOfCards: bigint
  numberOfDownloads: bigint
  isUserContains: boolean
}>();

const addLearningCollection = (learningCollectionId: number) => {
  const result = postLearningCollection(learningCollectionId);
  userLearningCollectionsStore.addUserLearningCollection(
      learningCollectionsStore.getById(BigInt(learningCollectionId))
  );
};

const removeLearningCollection = (learningCollectionId: number) => {
  const result = deleteLearningCollection(learningCollectionId);
  userLearningCollectionsStore.deleteUserLearningCollection(BigInt(learningCollectionId));
}
</script>

<template>
  <div class="learning-collection-card">
    <img class="preview-image" :src="learningCollectionImage"/>
    <div class="info">
      <span>Author id: <span class="highlight">{{props.ownerId}}</span></span>
      <span>Name: <span class="highlight">{{props.name}}</span></span>
      <span>Number of cards: <span class="highlight">{{props.numberOfCards}}</span></span>
      <span>Number of downloads: <span class="highlight">{{props.numberOfDownloads}}</span></span>
    </div>
    <blue-button v-if="!isUserContains" class="add-button" @click="addLearningCollection(props.id)">+</blue-button>
    <button v-else class="delete-button" @click="removeLearningCollection(props.id)">-</button>
  </div>
</template>

<style scoped>
.add-button {
  border-radius: 5px;
  width: 30px;
  height: 30px;
}

.delete-button {
  border: none;
  border-radius: 5px;
  color: white;
  width: 30px;
  height: 30px;
  font-size: 20px;
  font-weight: bold;
  background-color: #d10e2d;
}

.delete-button:hover {
  background-color: #e10a21;
}

.delete-button:active {
  background-color: #f60606;
}

.learning-collection-card {
  background-color: #08104E;
  box-sizing: border-box;
  width: 700px;
  height: 200px;
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 10px;
  gap: 20px;
}

.info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 20px;
  color: white;
  font-size: 16px;
}

.highlight {
  color: #FFAA00;
}
</style>
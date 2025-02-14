<script setup lang="ts">
import {LearningCollectionPreview} from "@/types/learningCollection";
import learningCollectionImage from "@/assets/default_learning_collection_image.png";
import {postLearningCollection} from "@/api/leaningCollectionService";

const props =  defineProps<LearningCollectionPreview>();

const addLearningCollection = (learningCollectionId: number) => {
  const result = postLearningCollection(learningCollectionId);
};
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
    <button class="add-button" @click="postLearningCollection(props.id)">+</button>
  </div>
</template>

<style scoped>
.add-button {
  border: none;
  border-radius: 5px;
  color: white;
  width: 30px;
  height: 30px;
  font-size: 20px;
  font-weight: bold;
  background-color: #3914AF;
}

.add-button:hover {
  background-color: #4012ce;
}

.add-button:active {
  background-color: #430ee8;
}


.learning-collection-card {
  background-color: #08104E;
  width: 700px;
  height: 200px;
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 10px;
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
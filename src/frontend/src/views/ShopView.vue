<script setup lang="ts">
import LearningCollectionPreview from "@/components/LearningCollectionPreview.vue";
import {useLearningCollectionsStore} from "@/stores/storeLearningCollections";
import {onMounted} from "vue";
import {useUserLearningCollectionsStore} from "@/stores/userLearningCollections";


const learningCollectionsStore = useLearningCollectionsStore();
const userLearningCollectionsStore = useUserLearningCollectionsStore();
const learningCollections = learningCollectionsStore.learningCollections;

onMounted(() => {
  userLearningCollectionsStore.fetchUserLearningCollections();
  learningCollectionsStore.fetchLearningCollections();
})
</script>

<template>
  <div>
    <div v-if="learningCollectionsStore.isLoaded && userLearningCollectionsStore.isLoaded" class="shop">
      <LearningCollectionPreview v-for="learningCollection in learningCollections"
                               :key="learningCollection.id"
                               :id="learningCollection.id"
                               :name="learningCollection.name"
                               :owner-id="learningCollection.ownerId"
                               :number-of-cards="learningCollection.numberOfCards"
                               :number-of-downloads="learningCollection.numberOfDownloads" :is-user-contains="userLearningCollectionsStore.isCollection(learningCollection.id)"/>
    </div>
    <div v-else>
      Loading...
    </div>
  </div>

</template>

<style scoped>
.shop {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
</style>
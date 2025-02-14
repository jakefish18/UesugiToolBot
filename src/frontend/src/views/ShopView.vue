<script setup lang="ts">
import LearningCollectionPreview from "@/components/LearningCollectionPreview.vue";
import {useLearningCollectionsStore} from "@/stores/storeLearningCollections";
import {onMounted} from "vue";


const learningCollectionsStore = useLearningCollectionsStore();
const learningCollections = learningCollectionsStore.learningCollections;

onMounted(() => {
  learningCollectionsStore.fetchLearningCollections();
})
</script>

<template>
  <div>
    <div v-if="learningCollectionsStore.isLoaded" class="shop">
      <LearningCollectionPreview v-for="learningCollection in learningCollections"
                               :key="learningCollection.id"
                               :id="learningCollection.id"
                               :name="learningCollection.name"
                               :owner-id="learningCollection.ownerId"
                               :number-of-cards="learningCollection.numberOfCards"
                               :number-of-downloads="learningCollection.numberOfDownloads"/>
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
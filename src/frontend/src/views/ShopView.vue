<script setup lang="ts">
import LearningCollectionPreview from "@/components/LearningCollectionPreview.vue";
import SearchInput from "@/components/SearchInput.vue";
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
  <div class="shop">
    <SearchInput/>
    <div v-if="learningCollectionsStore.isLoaded && userLearningCollectionsStore.isLoaded && learningCollections.length === 0" class="info-text">
      No collection found :(
    </div>
    <div v-else-if="learningCollectionsStore.isLoaded && userLearningCollectionsStore.isLoaded" class="shop-items">
      <LearningCollectionPreview v-for="learningCollection in learningCollections"
                                 :key="learningCollection.id"
                                 :id="learningCollection.id"
                                 :name="learningCollection.name"
                                 :owner-id="learningCollection.ownerId"
                                 :number-of-cards="learningCollection.numberOfCards"
                                 :number-of-downloads="learningCollection.numberOfDownloads"
                                 :is-user-contains="userLearningCollectionsStore.isCollection(learningCollection.id)"/>
    </div>
    <div v-else class="info-text">
      Loading...
    </div>
  </div>

</template>

<style scoped>
.info-text {
  margin-top: 20px;
  color: white;
  font-size: 20px;
}

.shop {
  align-items: center;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.shop-items {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
</style>
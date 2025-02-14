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
  <div class="shop">
    <LearningCollectionPreview v-for="learningCollection in learningCollections"
                               :key="learningCollection.id"
                               :id="learningCollection.id"
                               :name="learningCollection.name"
                               :owner-id="learningCollection.ownerId"
                               :number-of-cards="learningCollection.numberOfCards"
                               :number-of-downloads="learningCollection.numberOfDownloads"/>
  </div>
</template>

<script setup lang="ts">
import {LearningCollectionPreview} from "@/types/learningCollection";

const props =  defineProps<LearningCollectionPreview>();
</script>

<template>
  <div class="learning-collection-card">
      {{ props.id }}
  </div>
</template>

<style scoped>
.learning-collection-card {
  background-color: #08104E;
  width: 700px;
  height: 200px;
  border-radius: 5px;
}
</style>
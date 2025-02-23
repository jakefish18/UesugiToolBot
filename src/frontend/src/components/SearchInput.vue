<script setup lang="ts">
import SearchImg from "@/assets/Search.png";
import BlueButton from "@/components/BlueButton.vue";
import {useLearningCollectionsStore} from "@/stores/storeLearningCollections";
import { defineModel } from "vue";

const learningCollectoinsStore = useLearningCollectionsStore();
const searchQuery = defineModel<string>();


const searchLearningCollections = () => {
  if (searchQuery.value === undefined) {
    learningCollectoinsStore.searchLearningCollection("", BigInt(10), BigInt(0));
  } else {
    learningCollectoinsStore.searchLearningCollection(searchQuery.value!, BigInt(10), BigInt(0));
  }
};
</script>

<template>
  <div class="container">
    <input v-model="searchQuery" type="text" placeholder="Search..." class="search-input" @keyup.enter="searchLearningCollections"/>
    <blue-button @click="searchLearningCollections" class="search-button">
      <img class="search-button-img" :src="SearchImg"/>
    </blue-button>
  </div>
</template>

<style scoped>
.search-input {
  box-sizing: border-box;
  padding-left: 10px;
  width: 100%;
  height: 35px;
  border: none;
  border-radius: 3px 0px 0px 3px;
}

.search-input:focus {
  outline: none;
  border: 2px solid #ccc;
  border-color: #3914AF;
}

.search-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 35px;
  border: none;
  border-radius: 0px 3px 3px 0px;
}

.search-button-img {
  height: 26px;
  width: 26px;
  color: white;
}

.container {
  display: flex;
  align-self: center;
  width: 700px;
  gap: 0;
}
</style>
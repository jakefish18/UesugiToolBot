<template>
  <div class="center-items">
    <SearchBar class="search-bar"></SearchBar>
    <search-result-list></search-result-list>
  </div>
</template>

<script lang="js">
import SearchBar from "@/components/SearchBar";
import SearchResultList from "@/components/SearchResultList.vue";

export default {
  components: {
    SearchResultList,
    SearchBar
  }
}
</script>

<style scoped>

.center-items {
  display: flex;
  flex-direction: column;
  margin-left: 20%;
  gap: 30px;
}

</style>

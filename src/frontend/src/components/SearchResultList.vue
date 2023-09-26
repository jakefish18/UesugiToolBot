<script>
import SearchResult from "@/components/SearchResult";

export default {
  components: {
    SearchResult
  },
  name: "SearchResultList"
}
</script>

<template>
  <div class="search-result-list">
    <search-result></search-result>
  </div>
</template>

<style scoped>

.search-result-list {
  display: flex;
  flex-direction: column;
}

</style>
<template>
  <div class="search">
    <div class="search-bar">
      <SearchButton class="search-button search-bar-elem"></SearchButton>
      <SearchInput class="search-input search-bar-elem"></SearchInput>
    </div>
    <div class="sort-selector">
      <SortSelector></SortSelector>
    </div>
  </div>
</template>

<script lang="js">
import SearchButton from "@/components/SearchButton";
import SearchInput from "@/components/SearchInput";
import SortSelector from "@/components/SortSelector";

export default {
  components: {
    SearchButton,
    SearchInput,
    SortSelector
  }
};
</script>

<style scoped>

.search{
  display: flex;
  flex-direction: column;
}

.search-bar {
  display: flex;
  margin-top: 30px;
}

.sort-selector {
  margin-top: 10px;
  display: flex;
  align-items: center;
}
</style>

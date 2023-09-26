<template>
  <div class="search-input-div">
    <input
      class="search-input"
      type="text"
      placeholder="Поиск..."
      v-model="searchQuery"
    />
  </div>
</template>

<script lang="js">
export default {
    data() {
        return {
            searchQuery: ""
        }
    },
};
</script>

<style scoped>

.search-input {
  margin: 0;
  height: 40px;
  width: 900px;
  border: 0px;
  border-radius: 0px 8px 8px 0px;
  font-size: 20px;
  outline: none;
}

</style>

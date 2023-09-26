<template>
  <div class="search-button-div">
    <button class="search-button">
      <img class="search-icon" src="@/assets/button.png" alt="">
    </button>
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
.search-button {
  background: #3914AF;
  border: #3914AF;
  border-radius: 8px 0px 0px 8px;
  height: 42px;
  width: 60px;
}

.search-button:hover {
  background: #3A0AD1;
}

.search-button:active {
  background: #5E2FF5;
}

.search-icon {
  width: 30px;
  height: 30px;
}
</style>

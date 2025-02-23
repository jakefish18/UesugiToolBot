<script setup lang="ts">

</script>

<template>
  <button>
    <slot/>
  </button>
</template>

<style scoped>
button {
  border: none;
  color: white;
  font-size: 20px;
  font-weight: bold;
  background-color: #3914AF;
}

button:hover {
  background-color: #4012ce;
}

button:active {
  background-color: #430ee8;
}
</style>
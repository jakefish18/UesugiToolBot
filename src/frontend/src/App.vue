<script scoped>
import HeaderBar from "@/components/HeaderBar.vue";
import {defineComponent, onMounted} from "vue";
import { useUserStore } from "@/stores/user";

export default defineComponent({
  components: {HeaderBar}
})

</script>

<template>
  <HeaderBar></HeaderBar>
  <div class="router-container">
    <router-view/>
  </div>
</template>

<style>
body {
  margin: 0;
  padding: 0;
  background-color: #040720;
}

#app {
  font-family: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

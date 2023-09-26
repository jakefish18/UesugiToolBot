<template>
  <div class="app" id="app">
    <FooterBar></FooterBar>
    <SearchPage></SearchPage>
    <!-- <router-view></router-view> -->
  </div>
</template>

<script>
import SearchPage from "@/views/SearchPage";
import FooterBar from "@/components/FooterBar";

export default {
  name: "App",
  components: {
    SearchPage,
    FooterBar,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap");

body {
  margin: 0;
  padding: 0;
  border: 0;
  font-family: "Montserrat", sans-serif;
  background: #040720;
}
</style>

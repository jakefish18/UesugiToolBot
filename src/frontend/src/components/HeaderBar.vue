<script setup lang="ts">
import logoImage from "@/assets/logo.png"
import { useUserStore } from "@/stores/user";
import {onMounted} from "vue";

const userStore = useUserStore();
const user = userStore.user;

onMounted(() => {
  console.log("Fetching user");
  const userStore = useUserStore();
  userStore.fetchUser();
})
</script>

<template>
  <header>
    <div class="logo">
      <img class="logo-image" :src="logoImage" :alt="logo">
      <span class="site-name">UesugiToolHelper</span>
    </div>
    <nav>
      <ul>
        <li><router-link to="/shop" class="link">Shop</router-link></li>
        <li><router-link to="/editor" class="link">Editor</router-link></li>
      </ul>
    </nav>
    <div v-if="userStore.isLoggedIn" class="profile">
      ID: {{ user.id }}
    </div>
    <div v-else class="profile">
      ID: FAILED
    </div>
  </header>
</template>

<style scoped>
header {
  font-size: 16px;
  color: white;
}

.logo {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: left;
  gap: 10px;
  width: 300px;
}

.profile {
  width: 300px;
  display: flex;
  justify-content: right;
}

nav {
  height: 100%;
}

nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  height: 100%;
}

nav ul li {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
}

.site-name {
  font-size: 24px;
  color: white;
  font-weight: bold;
}

.logo-image {
  height: 55px;
}

.link {
  text-decoration: none;
  color: white;
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.link:hover {
  background-color: #151E6F;
}

.link:active {
  background-color: #232F95;
}

header {
  height: 65px;
  background-color: #08104E;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding-right: 10px;
  padding-left: 10px;
}
</style>

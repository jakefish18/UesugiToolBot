<script setup lang="ts">
import logoImage from "@/assets/logo.png"

</script>

<template>
  <header>
    <div class="logo">
      <img class="logo-image" :src="logoImage" :alt="logo">
      <span class="site-name">UesugiToolHelper</span>
    </div>
    <nav>
      <router-link to="/shop" class="link">Shop</router-link>
      <router-link to="/editor" class="link">Editor</router-link>
    </nav>
    <div class="profile">
      ID: ID
    </div>
  </header>
</template>

<style scoped>
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

.site-name {
  font-size: 24px;
  color: white;
  font-weight: bold;
}

.logo-image {
  height: 55px;
}

nav {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 10px;
}

nav .link {
  text-decoration: none;
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

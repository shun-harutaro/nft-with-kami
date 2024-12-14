<template>
  <a :href="loginUrl">
    <img src="@/assets/img/btn_login_base.png" alt="LINEでログイン" />
  </a>
</template>

<script setup>
import { ref } from 'vue';

const baseUrl = import.meta.env.VITE_API_URL;
const loginUrl = ref(`${baseUrl}/api/auth/login`);
</script>

<style scoped>
a {
  display: inline-block;
  text-decoration: none;
}

a img {
  width: 100%;
  height: auto;
}
</style>

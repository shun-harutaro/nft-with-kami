<template>
  <button @click="handleLogin">
    <img src="@/assets/img/btn_login_base.png" alt="LINEでログイン" />
  </button>
</template>

<script setup>
  const baseUrl = import.meta.env.VITE_API_URL;
  const loginUrl = new URL("/api/auth/login", baseUrl);
  const handleLogin = () => {
    window.location.href = loginUrl
  }
</script>

<style scoped>
button {
  padding: 0;
  border: none;
  background: none;
  display: inline-block;
  cursor: pointer;
}

button img {
  width: 100%;
  height: auto;
}
</style>

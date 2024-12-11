<template>
  <button @click="handleLogin">
    <img src="@/assets/img/btn_login_base.png" alt="LINEでログイン" />
  </button>
</template>

<script setup>
  const handleLogin = () => {
    window.location.href = "/api/auth/login"
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

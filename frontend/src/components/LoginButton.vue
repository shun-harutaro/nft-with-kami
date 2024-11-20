<template>
  <button @click="handleLogin">LINEでログイン</button>
</template>

<script>
import { useAuth } from "@/composables/useAuth";

export default {
  setup() {
    const { login } = useAuth();

    function handleLogin() {
      login();
    }

    return {
      handleLogin,
    };
  },
};
</script>

<template>
  <button @click="handleLogin">
    <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/4a8febd21bfe1feaeaa099720a3e2ffe159c07ff180a36ffd7064a04500b571c?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-footer"
        alt="Gallery Footer"
        />
  </button>
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

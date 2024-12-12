<script setup>
import { useRouter } from "vue-router";

const handleShare = () => {
  /* TODO: 実装 */
}

const handleReturn = () => {
  router.push("/")
}
</script>

<template>
  <div class="result-screen">
    <div class="share-container">
      <button
        class="share-button"
        @click="handleShare"
        aria-label="おみくじをシェア">
        <span>おみくじをシェア</span>
      </button>
    </div>
    <button
      class="return-button"
      @click="handleReturn"
      aria-label="最初へ戻る">
      最初へ戻る
    </button>
  </div>
</template>

<style scoped>
.result-screen {
  background-color: rgba(245, 239, 219, 1);
  display: flex;
  max-width: 100%;
  width: 100%;
  flex-direction: column;
  overflow: hidden;
  font-family: Noto Serif JP, sans-serif;
  color: rgba(0, 0, 0, 1);
  font-weight: 400;
  white-space: nowrap;
  margin: 0 auto;
  padding: 20px 10px;
  box-sizing: border-box;
  min-height: 100vh;
}

.share-container {
  display: flex;
  justify-content: center;
  font-size: 20px;
  text-align: center;
}

.share-button {
  border: 1px solid rgba(0, 0, 0, 1);
  background-color: rgba(255, 255, 255, 1);
  cursor: pointer;
  font-family: inherit;
  font-size: 16px;
  padding: 10px 20px;
  border-radius: 12px;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.share-button span {
  display: block;
  text-align: center;
}

.share-button:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
}

.return-button {
  border-radius: 50px;
  background-color: rgba(255, 242, 0, 1);
  align-self: center;
  margin-top: 20px;
  width: 100%;
  max-width: 300px;
  font-size: 24px;
  padding: 15px;
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.return-button:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>

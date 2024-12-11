<template>
  <div class="oracle-container">
    <div class="oracle-content">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/a4beab784bace2791631ccb9f774c9dbbf5b2a2dc8a297f456eadaebcac0dcc2?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
        class="background-image"
        alt=""
      />
      <!-- しめ縄 -->
      <div class="shimenawa-wrapper">
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/ca478b57abe97bbcce996dffe8452006b0a8bca14c89094a7818a306c0b1b889?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
          class="shimenawa-image"
          alt="Shimenawa"
        />
        <button 
          class="oracle-button" 
          tabindex="0" 
          role="button"
          aria-label="神託を得る"
          @click="handleClick"
          @keydown.enter="handleClick"
          @keydown.space="handleClick"
        >
          神託を<br />得る
        </button>
      </div>
      <button 
        class="view-history-button"
        @click="viewHistory"
        tabindex="0"
        role="button"
        aria-label="View past oracle prophecies"
      >
        過去の神託を見る
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'OracleHistory',
  methods: {
    viewHistory(): void {
      // Handle view history action
    },
    handleClick(): void {
      this.$router.push('/location');
    }
  }
})
</script>

<style scoped>
.oracle-container {
  background-color: #fff;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
  display: flex;
  max-width: 480px;
  width: 100%;
  flex-direction: column;
  overflow: hidden;
  color: #fff;
  white-space: nowrap;
  text-align: center;
  margin: 0 auto;
  font: 400 24px Noto Serif JP, sans-serif;
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.oracle-content {
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
  padding: 240px 0 52px;
}

.background-image {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

.shimenawa-wrapper {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  z-index: 10;
}

.shimenawa-image {
  width: 100%;
  object-fit: contain;
  object-position: center;
  z-index: 5; /* しめ縄を前面に表示 */
}

.oracle-button {
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-45%, -45%);
  background-color: rgba(255, 69, 0, 1);
  border: none;
  border-radius: 50%;
  color: rgba(255, 255, 255, 1);
  cursor: pointer;
  font: 400 50px 'Noto Serif JP', sans-serif;
  height: 200px; /* ボタンのサイズ */
  width: 200px;
  text-align: center;
  transition: transform 0.2s ease;
  z-index: 20; /* ボタンをしめ縄の後ろに配置 */
}

.oracle-button:hover,
.oracle-button:focus {
  outline: 3px solid rgba(255, 255, 255, 0.5);
  transform: scale(1.02);
}

.oracle-button:focus-visible {
  outline: 3px solid rgba(255, 255, 255, 0.8);
}

.oracle-button:active {
  transform: scale(0.98);
}

.view-history-button {
  position: relative;
  border-radius: 12px;
  background-color: #ff4500;
  align-self: center;
  width: 242px;
  max-width: 100%;
  padding: 24px 28px;
  border: 2px solid rgba(255, 215, 0, 0.4);
  color: #fff;
  font: inherit;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.view-history-button:hover,
.view-history-button:focus {
  background-color: #ff5722;
  outline: none;
}

.view-history-button:focus-visible {
  box-shadow: 0 0 0 3px rgba(255, 69, 0, 0.5);
}
</style>

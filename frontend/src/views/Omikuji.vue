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
    <div class="result-container">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/5e81f6d4ca789c8e3f9077e0b717f7c8b773568f91ec42fd69779d2e78a5813b?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
        class="background-image"
        alt=""
      />
      <div class="fortune-display"></div>
      <div class="share-section">
        <button 
	        class="share-button" 
	        tabindex="0"
	        @click="handleShare"
          aria-label="おみくじをシェア">
          <span>おみくじをシェア</span>
        </button>
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/1b3025bf1577dd0e3f2ae1f42ff1ae5f416bca32090785e1241417b7bc11443d?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
          class="share-icon"
          alt="Share fortune result"
        />
      </div>
      <button
         class="return-button"
         tabindex="0"
         @click="handleReturn"
         aria-label="最初へ戻る">
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/37658439fc1d41fe43bdb43b169f19d1626b20f05a953ebe1668ba8a62c7f442?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
          class="return-icon"
          alt=""
        />
        <span class="return-text">最初に戻る</span>
      </button>
    </div>
  </div>
</template>

<style scoped>
.result-screen {
  background-color: rgba(245, 239, 219, 1);
  display: flex;
  max-width: 480px;
  width: 100%;
  flex-direction: column;
  overflow: hidden;
  color: rgba(0, 0, 0, 1);
  font-weight: 400;
  text-align: center;
  margin: 0 auto;
}

.result-container {
  display: flex;
  flex-direction: column;
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
  padding: 174px 0 27px;
}

.background-image {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

.fortune-display {
  position: relative;
  display: flex;
  min-height: 395px;
  width: 100%;
}

.share-section {
  position: relative;
  display: flex;
  gap: 11px;
  font-size: 40px;
}

.share-button {
  align-self: start;
  flex-grow: 1;
  flex-basis: auto;
  border: 1px solid rgba(0, 0, 0, 1);
  background: none;
  cursor: pointer;
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  font-size: 30px;
}

.share-icon {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 70px;
}

.return-button {
  display: flex;
  flex-direction: column;
  position: relative;
  border-radius: 30px;
  box-shadow: 4px 20px 4px rgba(0, 0, 0, 0.5);
  align-self: center;
  aspect-ratio: 1.777;
  margin-top: 20px;
  width: 100%;
  max-width: 295px;
  font-size: 48px;
  padding: 61px 33px;
  border: 1px solid rgba(0, 0, 0, 1);
  background: none;
  cursor: pointer;
  font-family: inherit;
  color: inherit;
}

.return-icon {
  width: 100%;
  height: 100%;
  object-fit: contain;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.return-text {
  position: relative;
  z-index: 2;
  font-size: inherit;
  color: inherit;
  font-size: 45px;
  text-align: center;
}

</style>
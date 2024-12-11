<template>
    <div class="result-screen">
      <div class="fortune-image" role="img" aria-label="おみくじ結果"></div>
      <div class="share-container">
        <button 
          class="share-button" 
          @click="handleShare"
          aria-label="おみくじをシェア">
          おみくじをシェア
        </button>
        <img
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/1b3025bf1577dd0e3f2ae1f42ff1ae5f416bca32090785e1241417b7bc11443d?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
          class="share-icon"
          alt="シェアアイコン"
          loading="lazy"
        />
      </div>
      <button 
        class="return-button"
        @click="handleReturn"
        aria-label="最初へ戻る">
        最初へ戻る
      </button>
    </div>
  </template>
  
  <script lang="ts">
  import apiAxios from "@/plugin/axios";
  import { defineComponent } from 'vue'
  
  export default defineComponent({
    name: 'OmikujiResult',
    methods: {
      handleShare() {
        // Share functionality implementation
      },
      handleReturn() {
        this.$router.push('/')
      }
    }
  })
  </script>
  
  <style scoped>
  .result-screen {
    background-color: rgba(245, 239, 219, 1);
    display: flex;
    max-width: 480px;
    width: 100%;
    flex-direction: column;
    overflow: hidden;
    font-family: Noto Serif JP, sans-serif;
    color: rgba(0, 0, 0, 1);
    font-weight: 400;
    white-space: nowrap;
    margin: 0 auto;
    padding: 149px 0 15px;
  }
  
  .fortune-image {
    display: flex;
    min-height: 420px;
    width: 100%;
  }
  
  .share-container {
    display: flex;
    gap: 11px;
    font-size: 40px;
    text-align: center;
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
    padding: 10px;
  }
  
  .share-button:focus {
    outline: 2px solid #000;
    outline-offset: 2px;
  }
  
  .share-icon {
    aspect-ratio: 1;
    object-fit: contain;
    object-position: center;
    width: 70px;
  }
  
  .return-button {
    border-radius: 100px;
    background-color: rgba(255, 242, 0, 1);
    align-self: center;
    margin-top: 105px;
    width: 346px;
    max-width: 100%;
    font-size: 48px;
    padding: 30px 70px 19px;
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
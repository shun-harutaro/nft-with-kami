<template>
    <div class="omikuji-screen">
      <div class="content-wrapper">
        <img
          loading="lazy"
          src="@/assets/img/god-background.png"
          class="background-image"
          alt=""
        />
        <div class="generation-status">おみくじ生成中！</div>
        <div class="kamisama-container"></div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .omikuji-screen {
    background-color: rgba(245, 239, 219, 1);
    display: flex;
    max-width: 480px;
    width: 100%;
    flex-direction: column;
    overflow: hidden;
    color: rgba(0, 0, 0, 1);
    white-space: nowrap;
    text-align: center;
    margin: 0 auto;
    font: 400 48px Noto Serif JP, sans-serif;
  }
  
  .content-wrapper {
    display: flex;
    flex-direction: column;
    position: relative;
    aspect-ratio: 0.461;
    width: 100%;
    padding: 45px 0 1px;
  }
  
  .background-image {
    position: absolute;
    inset: 0;
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }
  
  .generation-status {
    position: relative;
    align-self: start;
    border: 1px solid rgba(0, 0, 0, 1);
  }
  
  .kamisama-container {
    position: relative;
    display: flex;
    min-height: 737px;
    margin-top: 25px;
    width: 100%;
  }
  </style>
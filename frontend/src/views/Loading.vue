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
        <div class="kamisama-container">
          <img
            loading="lazy"
            src="@/assets/img/god.png"
            class="hero-foreground"
            alt=""
          />
        </div>
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
    aspect-ratio: 0.73;
    object-fit: contain;
    object-position: center;
    width: 100%;
    z-index: 10;
  }

  .hero-foreground {
    aspect-ratio: 0.73;
    object-fit: contain;
    object-position: center;
    width: 100%;
    z-index: 20;
    position: absolute; /* 神様を自由に配置するためにabsoluteを指定 */
    bottom: 10px; /* 下に配置 */
    left: 0;
    right: 0;
  }
  </style>
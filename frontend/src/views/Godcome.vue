<script setup>
const fetchShrine = () => {
  /* TODO 実装 */
}
</script>

<template>
    <section class="hero-section" role="banner">
      <img
        loading="lazy"
        src="@/assets/img/god-background.png"
        class="hero-background"
        alt=""
      />
      <img
        loading="lazy"
        src="@/assets/img/god.png"
        class="hero-foreground"
        alt=""
      />
    </section>
  </template>

  <style scoped>
  .hero-section {
    display: flex;
    flex-direction: column;
    position: relative;
    aspect-ratio: 0.461;
    width: 100%;
    padding: 311px 0 0;
  }

  .hero-background {
    position: absolute;
    inset: 0;
    height: 100%;
    width: 100%;
    object-fit: cover;
    object-position: center;
  }

  .hero-foreground {
    aspect-ratio: 0.73;
    object-fit: contain;
    object-position: center;
    width: 100%;
    z-index: 10;

    /* フェードアニメーション */
    opacity: 0;
    animation: fadeIn 2s ease-in forwards;
  }

  /* アニメーション定義 */
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
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

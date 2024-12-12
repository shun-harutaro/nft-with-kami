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
      <div class="omikuji-image">
        <img
          loading="lazy"
          src="@/assets/img/omikuji.png"
          class="rotating-image"
          alt="おみくじ"
        />
      </div>
      <div class="godtalk-status">しばし待つのじゃ！</div>
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
  font: 400 48px;
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
  align-self: center;
  justify-content: center;
  border: 1px solid rgba(0, 0, 0, 1);
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 40px;
  z-index: 30;
}

.godtalk-status {
  position: absolute;
  bottom: 150px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 5px;
  font-size: 30px;
  z-index: 30;
  text-align: center;
}

.omikuji-image {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
}

.rotating-image {
  width: 150px;
  height: auto;
  animation: spin-and-stop 4s ease-in-out infinite;
}

@keyframes spin-and-stop {
  0% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(720deg);
  }
  100% {
    transform: rotate(1440deg);
  }
}

/* 神様の激しいランダムな荒ぶり */
@keyframes god-chaos {
  0% {
    transform: translate(0px, 0px) scale(1);
  }
  10% {
    transform: translate(-5px, -5px) scale(1.05);
  }
  20% {
    transform: translate(5px, -10px) scale(0.95);
  }
  30% {
    transform: translate(-10px, 5px) scale(1.1);
  }
  40% {
    transform: translate(10px, 10px) scale(1);
  }
  50% {
    transform: translate(-5px, -5px) scale(1.05);
  }
  60% {
    transform: translate(5px, -10px) scale(0.9);
  }
  70% {
    transform: translate(-10px, 5px) scale(1.2);
  }
  80% {
    transform: translate(10px, 0px) scale(1);
  }
  90% {
    transform: translate(0px, -10px) scale(1.1);
  }
  100% {
    transform: translate(0px, 0px) scale(1);
  }
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
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
  animation: god-chaos 0.5s linear infinite; /* ランダムで小刻みに動くアニメーション */
}
</style>

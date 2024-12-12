<script setup>
import { computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useUserProfileStore } from "@/stores/userProfileStore";
import LoginButton from "@/components/LoginButton.vue"

const router = useRouter();

// ストアのインスタンスを取得
const userStore = useUserProfileStore();

// ログイン状態とユーザー情報を取得
const isLoggedIn = computed(() => userStore.isLoggedIn);
const displayName = computed(() => userStore.displayName);
const profileImageUrl = computed(() => userStore.profileImageUrl);

// 初期化処理: コンポーネントのマウント時にプロフィールを取得
onMounted(() => {
  userStore.fetchUserProfile();
});

const viewHistory = () => {
  /* TODO: 実装 */
}

const handleClick = () => {
  router.push("/location")
}
</script>


<template>
  <div class="gallery-container">
    <div class="gallery-wrapper">
      <img
        loading="lazy"
        src="@/assets/img/new_background.png"
        class="gallery-background"
        alt="背景画像(神社)"
      />
      <img
        loading="lazy"
        src="@/assets/img/nft-with-kami-logo.png"
        class="gallery-header"
        alt="NFTwith神ロゴ"
      />
      <img
        loading="lazy"
        src="@/assets/img/background-shrine-alpha.png"
        class="gallery-overlay"
        alt="しめ縄"
      />

      <div v-if="isLoggedIn">
        <button
          class="oracle-button"
          @click="handleClick"
        >
          神託を<br/>得る
        </button>
        <button
          class="view-history-button"
          style="position: absolute; bottom: 20px; left: 20px;"
          @click="viewHistory"
        >
          過去の神託を見る
        </button>
      </div>
      <div v-else>
        <LoginButton
          style="position: absolute; z-index: 10; transform: scale(1); top: 750px; left: 50%; transform: translateX(-50%) scale(1.25);" />
      </div>
    </div>
  </div>
</template>


<style scoped>
.gallery-container {
  background: linear-gradient(to bottom, #35ECBB, #FF9C12);
  display: flex;
  max-width: 480px;
  width: 100%;
  flex-direction: column;
  overflow: hidden;
  margin: 0 auto;
}

.gallery-wrapper {
  display: flex;
  flex-direction: column;
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
  padding: 106px 0;
}

.gallery-background,
.gallery-overlay {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

.gallery-header {
  aspect-ratio: 1.22;
  object-fit: contain;
  object-position: center;
  width: 219px;
  max-width: 100%;
  z-index:10 ;
}

.gallery-content {
  aspect-ratio: 1.26;
  object-fit: contain;
  object-position: center;
  width: 100%;
  margin-top: 89px;
  position: relative;
  top: 20px;
}

.gallery-footer {
  aspect-ratio: 3.45;
  object-fit: contain;
  object-position: center;
  width: 207px;
  align-self: center;
  max-width: 100%;
  position: relative;
  top: 50px;
  z-index: 100000;
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

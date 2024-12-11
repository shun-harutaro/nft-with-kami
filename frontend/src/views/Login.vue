<script setup>
import { computed, onMounted } from "vue";
import { useUserProfileStore } from "@/stores/userProfileStore";
import LoginButton from "@/components/LoginButton.vue"

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

// ログアウト処理
const handleLogout = () => {
  userStore.logout();
};
</script>


<template>
<div class="gallery-container">
<div class="gallery-wrapper">
<!--神社-->
<img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/03f63f5fe13b4cb994f7f82af912ed64800f4fba07839ebe49c033b475648fea?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-background"
        alt=""
      />
<!--NFTwith神-->
<img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/746a97cb32fcc0e663949dd8a4e00662dd6fb2957f4ffb8fcbbd6411133003e9?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-header"
        alt="Gallery Header"
      />
<!--太陽モワモワ-->
<img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/d58f3000989a01d360aa6b718bf2a1da619b65250a41c5c91f8d6192282d4246?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-content"
        alt="Gallery Content"
      />
    <!--LINEログイン-->
    <div v-if="isLoggedIn" style="position: absolute; z-index: 10; transform: scale(1); top: 750px; left: 50%; transform: translateX(-50%) scale(1.25);" >
      <router-link to="/shintaku">神託の画面へ</router-link>
    </div>
    <div v-else>
      <LoginButton style="position: absolute; z-index: 10; transform: scale(1); top: 750px; left: 50%; transform: translateX(-50%) scale(1.25);" />
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

.gallery-background {
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
</style>

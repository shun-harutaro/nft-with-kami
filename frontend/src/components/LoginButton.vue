<template>
  <div>
    <a v-if="isUrlFetched" :href="redirectUrl" @click.prevent="handleClick">
      <img src="@/assets/img/btn_login_base.png" alt="LINEでログイン" />
    </a>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const redirectUrl = ref("#"); // 初期値をダミーURLに設定
const isUrlFetched = ref(false); // URLが取得できたかどうかを管理

// ログインURLを取得する関数
const fetchLoginUrl = async () => {
  try {
    const response = await axios.get("/api/auth/url");
    redirectUrl.value = response.data.redirect_url; // APIから取得したURLを設定
    isUrlFetched.value = true; // URL取得フラグを更新
  } catch (error) {
    console.error("ログインURLの取得に失敗しました:", error);
  }
};

// ボタンクリック時の処理
const handleClick = () => {
  if (isUrlFetched.value) {
    window.location.href = redirectUrl.value; // URLが取得されていればリダイレクト
  }
};

// コンポーネントマウント時にログインURLをフェッチ
onMounted(() => {
  fetchLoginUrl();
});
</script>

<style scoped>
a {
  display: inline-block;
  text-decoration: none;
}

a img {
  width: 100%;
  height: auto;
}
</style>

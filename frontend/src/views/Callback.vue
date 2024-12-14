<template>
  <div>
    <p v-if="loading">読み込み中...</p>
    <p v-else-if="error">エラーが発生しました: {{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const loading = ref(true); // ローディング状態を管理
const error = ref(null); // エラー状態を管理
const router = useRouter(); // ルーターの使用

onMounted(async () => {
  try {
    const urlParams = new URLSearchParams(window.location.search); // クエリパラメータを取得

    // code と state をバックエンドに送信
    const response = await axios.get('/api/auth/token', {
      params: {
        code: urlParams.get('code'),
        state: urlParams.get('state')
      }
    });

    console.log(response.data); // レスポンスデータを表示（任意）

    // トークン取得後、指定したルートにリダイレクト
    router.push('/'); // 例えばホームページにリダイレクト

  } catch (err) {
    error.value = err.message || "不明なエラーが発生しました";
  } finally {
    loading.value = false; // ローディング完了
  }
});
</script>

<style scoped>
p {
  font-size: 1.2rem;
}
</style>

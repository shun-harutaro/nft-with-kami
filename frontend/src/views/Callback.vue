<template>
  <div v-if="loading">認証中...</div>
  <div v-else>
    <p v-if="token">認証が完了しました。</p>
    <p v-if="error">認証エラー: {{ error }}</p>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuth } from "@/composables/useAuth";  // useAuthの利用

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const { getToken } = useAuth();

    const loading = ref(true);
    const token = ref(null);
    const error = ref(null);

    onMounted(async () => {
      const queryParams = route.query;

      const { code, state, friendship_status_changed } = queryParams;

      // 1. state を検証
      if (state !== localStorage.getItem("authState")) {
        error.value = "CSRF攻撃の疑いがあります。";
        loading.value = false;
        return;
      }

      // 2. code をバックエンドに送信してアクセストークンを取得
      try {
        token.value = await getToken(code);

        // ログイン後、ダッシュボードやホーム画面へリダイレクト
        //router.push("/dashboard");

      } catch (err) {
        error.value = "アクセストークンの取得に失敗しました。";
      } finally {
        loading.value = false;
      }
    });

    return {
      loading,
      token,
      error,
    };
  },
};
</script>

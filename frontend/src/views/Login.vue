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
  <div>
    <div v-if="isLoggedIn">
      <div class="profile">
        <img :src="profileImageUrl" alt="Profile Image" class="profile-image" />
        <p>ようこそ、{{ displayName }}さん！</p>
      </div>
      <button @click="handleLogout">ログアウト</button>
    </div>
    <div v-else>
      <p>ログインしてください。</p>
      <LoginButton />
    </div>
  </div>
</template>

<style scoped>
.profile {
  display: flex;
  align-items: center;
}
.profile-image {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}
</style>

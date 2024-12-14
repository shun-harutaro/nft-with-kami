<script setup>
import axios from "axios";
import { ref, computed, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useUserProfileStore } from "@/stores/userProfileStore";

const router = useRouter();
const route = useRoute();

const threadId = ref("");
const userProfileStore = useUserProfileStore();
const profileImageUrl = computed(() => userProfileStore.profileImageUrl);

// チャットのサマリーを取得
const fetchChatSummary = async () => {
  const response = await axios.post(`/api/gpt/chat-summary?thread_id=${threadId.value}`);
  return response.data;
};

// おみくじのテキストを取得
const fetchOmikuji = async (summaryText, updatedThreadId) => {
  const response = await axios.post(`/api/gpt/omikuji?text=${summaryText}&thread_id=${updatedThreadId}`);
  return response.data.text;
};

// JSON形式のテキストと神社情報を取得
const fetchJsonCreate = async (summaryText, updatedThreadId) => {
  const response = await axios.post(`/api/gpt/json`, {
    text: summaryText,
    thread_id: updatedThreadId,
  });
  return {
    omikujiText_json: `{${response.data.text}}`,
    shrineName: response.data.shrineName,
  };
};

// おみくじ画像を生成し、NFTメタデータを取得
const fetchCreatePhoto = async (omikujiText_json, shrineName) => {
  const imageResponse = await axios.post(
    `/api/omikuzi?shrine_name=${encodeURIComponent(shrineName)}&icon_url=${encodeURIComponent(profileImageUrl.value)}`,
    omikujiText_json,
    { headers: { "Content-Type": "application/json" }, responseType: "blob" }
  );

  const formData = new FormData();
  formData.append("upload_file", imageResponse.data, "omikuzi.png");

  const metadataResponse = await axios.post(`/api/nft`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return {
    photo: metadataResponse.data.image,
    tokenId: metadataResponse.data.tokenId,
    transactionHash: metadataResponse.data.transactionHash,
  };
};

// おみくじページに遷移
const navigateToOmikujiPage = (photo, tokenId, transactionHash) => {
  router.push({
    path: "/Omikuji",
    query: { photo, tokenId, transactionHash },
  });
};

// メインフロー
const fetchSummaryAndOmikuji = async () => {
  try {
    const { summaryText, updatedThreadId } = await fetchChatSummary();
    const { omikujiText_json, shrineName } = await fetchJsonCreate(summaryText, updatedThreadId);
    const { photo, tokenId, transactionHash } = await fetchCreatePhoto(omikujiText_json, shrineName);
    navigateToOmikujiPage(photo, tokenId, transactionHash);
  } catch (error) {
    console.error("Error during flow:", error);
    alert("エラーが発生しました。もう一度お試しください。");
  }
};

// 初期化処理
onMounted(() => {
  const queryThreadId = route.query.threadId;
  if (!queryThreadId) {
    alert("スレッドIDが見つかりません。最初からやり直してください。");
    return;
  }
  threadId.value = queryThreadId;
  fetchSummaryAndOmikuji();
});
</script>

<template>
  <div class="omikuji-screen">
    <div class="content-wrapper">
      <img id="icon">
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

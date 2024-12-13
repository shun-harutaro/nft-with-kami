<script>

import axios from 'axios';
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { computed } from "vue";
import { useUserProfileStore } from "@/stores/userProfileStore";

export default {
  data() {
    return {
      threadId: "", // 初期化されたスレッドID
    };
  },
  methods: {
    async fetchSummaryAndOmikuji() {
      try {
        // 1. /gpt/chat-summary エンドポイントを呼び出し
        console.log("Fetching chat summary with threadId:", this.threadId);
        const summaryResponse = await axios.post(`/api/gpt/chat-summary?thread_id=${this.threadId}`);
        const { text: summaryText, thread_id: updatedThreadId } = summaryResponse.data;

        console.log("Chat summary fetched:", summaryText);

        // 2. /gpt/omikuji エンドポイントを呼び出し
        console.log("Fetching omikuji with summary text and updated threadId...");
        const omikujiResponse = await axios.post(`/api/gpt/omikuji?text=${summaryText}&thread_id=${updatedThreadId}`);

        const { text: omikujiText } = omikujiResponse.data;

        console.log("Omikuji fetched:", omikujiText);
        //LINEアイコン取得
        const userProfileStore = useUserProfileStore();
        const profileImageUrl = computed(() => userProfileStore.profileImageUrl);
        console.log(profileImageUrl.value);

        // おみくじ画像生成リクエスト
        const blobUrl = ref(null);
        const picture = "https://tyoudoii-illust.com/wp-content/uploads/2024/07/oksign_businessman_simple-300x282.png";
        console.log("2");
        const response = await axios.post(
          `/api/omikuzi?shrine_name=${encodeURIComponent(shrinename)}&icon_url=${encodeURIComponent(profileImageUrl.value)}`,
            omikujiText,
          {
          headers: {
            'Content-Type': 'application/json'
          },
            responseType: 'blob' // 画像をblobで受け取る
          }
        );
        console.log("3");
        console.log("ここまでできてるよ");



      // NFTメタデータ取得用のリクエスト
      // NFTエンドポイントでファイルアップロードが必要な場合の例
      const formData = new FormData();
      formData.append("upload_file", response.data, "omikuzi.png");

      const metadataResponse = await axios.post(
        `/api/nft`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      );  
      console.log("NFT Token ID:", metadataResponse.data.tokenId);

        // 3. /Omikuji ページに遷移
        console.log("Navigating to /Omikuji with omikuji text...");
        this.$router.push({
          path: "/Omikuji",
          query: {
            text: omikujiText,
            photo: metadataResponse.image,
            tokenId: metadataResponse.data.tokenId,
            transactionHash: metadataResponse.data.transactionHash
          },
        });
      } catch (error) {
        console.error("Error during fetching or navigation:", error);
        alert("エラーが発生しました。もう一度お試しください。");
      }
    },
  },
  mounted() {
    // クエリパラメータから threadId を取得
    const { threadId } = this.$route.query;

    console.log(threadId)

    if (!threadId) {
      console.error("Missing threadId in query parameters.");
      alert("スレッドIDが見つかりません。最初からやり直してください。");
      return;
    }

    // スレッドIDを設定
    this.threadId = threadId;

    // フローを開始
    this.fetchSummaryAndOmikuji();
  },
};


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

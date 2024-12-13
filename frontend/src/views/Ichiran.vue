<template>
  <section class="history-container">
    <div class="history-wrapper">
      <img
        loading="lazy"
        src="@/assets/img/new_background.png"
        class="background-image"
        alt=""
      />
      <!-- タイトル -->
      <h1 class="title">過去のおみくじ一覧</h1>
      <div class="content-wrapper">
        <img
          loading="lazy"
          src="@/assets/img/background-shrine-alpha.png"
          class="overlay-image"
          alt=""
        />
        <div class="history-list">
          <!-- 配列からURLと作成年月日を利用 -->
          <template v-for="([url, date], index) in imageList" :key="index">
            <img
              loading="lazy"
              :src="url"
              class="fortune-image"
              :alt="`Fortune result for image ${index}`"
              @click="openModal(url)"
            />
            <time class="date-text">{{ date }}</time>
          </template>
        </div>
      </div>
      <!-- 戻るボタン -->
      <button class="back-button" @click="goBack">戻る</button>
    </div>
    
    <!-- モーダル -->
    <div v-if="isModalOpen" class="modal" @click="closeModal">
      <div class="modal-content" @click.stop>
        <img :src="modalImageUrl" class="modal-image" alt="Expanded fortune image" />
        <button class="close-button" @click="closeModal">×</button>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      imageList: [], // [[URL, 作成年月日], ...] の形式に変換して保存
      isModalOpen: false, // モーダルの表示状態
      modalImageUrl: "", // モーダルで表示する画像のURL
    };
  },
  methods: {
    // サーバーから画像 URL と作成年月日を取得
    async fetchImageList() {
      try {
        const response = await axios.get("/api/nft/users");

        // レスポンスが [{ image_url, created_at }, ...] の形式であることを想定
        if (response.data && Array.isArray(response.data)) {
          this.imageList = response.data.map((item) => [item.image_url, item.created_at]);
        } else {
          console.error("Unexpected response format:", response.data);
        }
      } catch (error) {
        console.error("Failed to fetch image list:", error);
      }
    },
    // 戻るボタンの動作
    goBack() {
      this.$router.go(-1); // 前のページに戻る
    },
    // モーダルを開く
    openModal(url) {
      this.modalImageUrl = url;
      this.isModalOpen = true;
    },
    // モーダルを閉じる
    closeModal() {
      this.isModalOpen = false;
      this.modalImageUrl = "";
    },
  },
  mounted() {
    // コンポーネントがマウントされたらデータを取得
    this.fetchImageList();
  },
};
</script>

<style scoped>
/* 全体のコンテナ */
.history-container {
  background-color: #fff;
  display: flex;
  max-width: 480px;
  width: 100%;
  flex-direction: column;
  overflow: hidden;
  color: #000;
  white-space: nowrap;
  text-align: center;
  margin: 0 auto;
  font: inherit;
}

/* 履歴のラッパー */
.history-wrapper {
  display: flex;
  flex-direction: column;
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
}

.background-image {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

/* タイトルのスタイル（背景内に配置） */
.title {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 40px!important; /* フォントサイズを大きく */
  font-weight: bold;
  color: #ffffff; /* 白で背景とコントラストをつける */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* 文字に影をつけて視認性を向上 */
  z-index: 1;
  font: inherit;
}

/* コンテンツラッパー */
.content-wrapper {
  display: flex;
  flex-direction: column;
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
  padding-top: 188px;
}

/* 履歴リスト */
.history-list {
  position: relative;
  display: flex;
  width: 100%;
  flex-direction: column;
  padding: 25px 51px;
}

/* 日付テキスト */
.date-text {
  position: relative;
  align-self: center;
  z-index: 10;
  margin-top: 20px;
  margin-bottom: 20px;
  font-weight: bold;
  color: #333;
  font-size: 36px;
  font: inherit;
}

.date-text::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 120%;
  height: 140%;
  background-color: #ffffff;
  border-radius: 10px;
  z-index: -1;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

/* おみくじ画像 */
.fortune-image {
  aspect-ratio: 1.78;
  object-fit: contain;
  object-position: center;
  width: 100%;
}

.fortune-image:not(:first-child) {
  margin-top: 30px;
}

/* オーバーレイ画像 */
.overlay-image {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

/* 戻るボタン */
.back-button {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 12px;
  background-image: url('@/assets/img/location-header.png');
  background-size: cover;
  background-position: center;
  background-color: transparent;
  border: none;
  align-self: center;
  width: 200px;
  max-width: 100%;
  padding: 24px 28px;
  border: 2px solid rgba(255, 215, 0, 0.4);
  color: #fff;
  font-size: 36px;
  font: inherit;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.back-button:hover {
  background-color: #e03e00;
}

/* モーダルスタイル */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 10px;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: transparent;
  color: #fff;
  font-size: 24px;
  border: none;
  cursor: pointer;
}
</style>

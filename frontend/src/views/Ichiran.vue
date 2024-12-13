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
              />
              <time class="date-text">{{ date }}</time>
            </template>
          </div>
        </div>
        <!-- 戻るボタン -->
        <button class="back-button" @click="goBack">戻る</button>
      </div>
    </section>
  </template>
  
  
  <script>
import { computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useUserProfileStore } from "@/stores/userProfileStore";
import axios from "axios";




  export default {
  data() {
    return {
      imageList: [], // [[URL, 作成年月日], ...] の形式に変換して保存
    };
  },
  methods: {
    // サーバーから画像 URL と作成年月日を取得
    async fetchImageList() {
      try {
        const response = await axios.get("/api/nft/users");

        // レスポンスが [{ image_url, created_at }, ...] の形式であることを想定
        if (response.data && Array.isArray(response.data)) {
          this.imageList = response.data.map(item => [item.image_url, item.created_at]);
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
  position: relative; /* 擬似要素を配置するために必要 */
  align-self: center;
  z-index: 10;
  margin-top: 20px; /* 上に少し余白を追加 */
  margin-bottom: 20px; /* 下に余白を追加 */
  font-weight: bold;
  color: #333; /* テキストの色 */
  font-size: 36px; /* 日付のフォントサイズを大きく */
  font: inherit;
}

.date-text::before {
  content: ""; /* 空のコンテンツを指定 */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* 中央揃え */
  width: 120%; /* 四角形の幅を少し広く */
  height: 140%; /* 四角形の高さを少し広く */
  background-color: #ffffff; /* 背景色を白に設定 */
  border-radius: 10px; /* 角を丸くする */
  z-index: -1; /* テキストより後ろに配置 */
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* 影をつける */
}

/* おみくじ画像 */
.fortune-image {
  aspect-ratio: 1.78;
  object-fit: contain;
  object-position: center;
  width: 100%;
}

.fortune-image:not(:first-child) {
  margin-top: 30px; /* 画像間の間隔を広げる */
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
  position: absolute; /* 元の位置調整の機能を保持 */
  bottom: 20px; /* 背景画像の下部に配置 */
  left: 50%; /* 中央揃え */
  transform: translateX(-50%); /* 中央揃えの補正 */
  border-radius: 12px; /* 新しいデザインの角丸 */
  background-image: url('@/assets/img/location-header.png'); /* 添付画像を背景に設定 */
  background-size: cover; /* ボタン全体に画像を調整 */
  background-position: center; /* 画像を中央揃え */
  background-color: transparent; /* 背景色を透明に設定 */
  border: none; /* 境界線を削除 */
  border-radius: 0; /* 不要な丸みを削除 */
  align-self: center; /* セルフ中央揃え（位置には影響なし） */
  width: 200px; /* 固定幅 */
  max-width: 100%; /* レスポンシブ調整 */
  padding: 24px 28px; /* 新しいパディング */
  border: 2px solid rgba(255, 215, 0, 0.4); /* ゴールド系の半透明ボーダー */
  color: #fff; /* テキストの色を白に */
  font-size: 36px; /* ボタンの文字サイズを大きく */
  font: inherit; /* 継承フォント設定 */
  cursor: pointer; /* クリック可能に */
  transition: background-color 0.2s ease; /* 背景色の変更アニメーション */
}

.back-button:hover {
  background-color: #e03e00; /* ホバー時に背景色を少し暗くする */
}


  </style>
  
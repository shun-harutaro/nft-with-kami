<template>
  <div class="shrine-selection">
    <!-- 全体の背景画像 -->
    <div class="background-container">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/857f846126a086104345dd3eb693dd2974c0f03dad83d569ba56dbca3c2cd40a?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
        class="background-image"
        alt="Shrine selection background"
      />
    </div>
    <!-- ヘッダー部分 -->
    <div class="header-section">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/c7570a0aa448614fd8f56816de33018bbd42534a73ed20ac0749d9aaa30e1648?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
        class="header-image"
        alt="Header decoration"
      />
      <h1 class="header-title">近くの神社</h1>
    </div>
    <!-- 神社リスト -->
    <div class="shrine-list">
      <div
        v-for="shrine in shrines"
        :key="shrine.name"
        class="shrine-item"
        @click="selectShrine(shrine)"
      >
        <div class="shrine-info">
          <img
            src="https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/geocode-71.png"
            class="shrine-icon"
            alt="Shrine icon"
          />
          <h2 class="shrine-name">{{ shrine.name }}</h2>
        </div>
        <span class="distance">{{ shrine.distance }}</span>
      </div>
    </div>
    <!-- 選択した神社の詳細 -->
    <div v-if="selectedShrine" class="selected-shrine">
      <h2>選択した神社</h2>
      <p><strong>名前:</strong> {{ selectedShrine.name }}</p>
      <p><strong>住所:</strong> {{ selectedShrine.address }}</p>
      <button class="select-button" @click="navigateToGodcome">選択する</button>
    </div>
    <!-- ローディング中やエラー表示 -->
    <div v-if="loading" class="loading">ロード中...</div>
    <div v-if="!loading && shrines.length === 0 && !error" class="no-shrines">
      神社が見つかりませんでした。
    </div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import apiAxios from "@/plugin/axios";

export default {
  data() {
    return {
      shrines: [], // 神社リスト
      selectedShrine: null, // 選択された神社
      loading: false, // ローディング状態
      error: null, // エラー情報
    };
  },
  created() {
    this.getLocation();
  },
  methods: {
    async getLocation() {
      if (navigator.geolocation) {
        this.loading = true;
        this.error = null;
        this.shrines = [];
        this.selectedShrine = null;

        navigator.geolocation.getCurrentPosition(
          async (position) => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            try {
              const response = await apiAxios.get("/api/location", {
                params: { latitude, longitude },
              });
              if (response.data && response.data.shrines) {
                this.shrines = response.data.shrines.map((shrine) => ({
                  name: shrine.name,
                  address: shrine.address,
                  distance: shrine.distance,
                }));
              } else {
                this.error = "データの取得に失敗しました。";
              }
            } catch (err) {
              this.error = "サーバーとの通信に失敗しました。";
            } finally {
              this.loading = false;
            }
          },
          () => {
            this.error = "位置情報の取得に失敗しました。";
            this.loading = false;
          }
        );
      } else {
        this.error = "位置情報が利用できません。";
      }
    },
    selectShrine(shrine) {
      this.selectedShrine = shrine;
    },
    navigateToGodcome() {
      this.$router.push({ path: "./Godcome", query: { shrine: this.selectedShrine.name } });
    },
  },
};
</script>

<style scoped>
/* 全体のスタイル */
.shrine-selection {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  margin: 0 auto;
  font-family: "Noto Serif JP", sans-serif;
  text-align: center;
}

/* 背景画像 */
.background-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  overflow: hidden;
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* ヘッダー部分 */
.header-section {
  position: relative;
  width: 100%;
  text-align: center;
  margin-bottom: 20px;
}

.header-image {
  width: 100%;
  height: auto;
}

.header-title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: clamp(24px, 8vw, 64px); /* 動的フォントサイズ */
  font-weight: bold;
  color: #fff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

/* 神社リスト */
.shrine-list {
  width: 100%;
  padding: 10px 0;
}

.shrine-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #ddd;
  padding: 10px 20px;
  background-color: rgba(255, 255, 255, 0.9);
  cursor: pointer;
  transition: background-color 0.2s;
}

.shrine-item:hover {
  background-color: rgba(255, 255, 255, 1);
}

.shrine-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.shrine-icon {
  width: 30px;
  height: 30px;
}

.shrine-name {
  font-size: 4vw;
  font-weight: bold;
  color: #333;
}

.distance {
  font-size: 3.5vw;
  color: #666;
}

/* 選択された神社 */
.selected-shrine {
  margin-top: 20px;
  padding: 10px;
  border: 2px solid #000000; /* 黒の枠を追加 */
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.9);
  text-align: center;
}

.selected-shrine h2 {
  font-size: 4vw;
  font-weight: bold;
}

.selected-shrine p {
  font-size: 3.5vw;
  margin: 5px 0;
}

.select-button {
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 3.5vw;
  background-color: #ffffff;
  color: #000000;
  border: 2px solid #000000; /* 黒の枠を追加 */
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  text-align: center;
}

.select-button:hover {
  background-color: #0056b3;
}

/* エラーおよび空リストメッセージ */
.error,
.no-shrines {
  margin-top: 20px;
  font-size: 4vw;
  color: #ff0000;
}

/* ローディング中 */
.loading {
  font-size: 4vw;
  color: #333;
  margin-top: 20px;
}
</style>

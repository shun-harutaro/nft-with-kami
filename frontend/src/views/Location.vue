<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

// データのリアクティブ変数
const shrines = ref([]); // 神社リスト
const selectedShrine = ref(null); // 選択された神社
const loading = ref(false); // ローディング状態
const error = ref(null); // エラー情報

// ルーターインスタンスの取得
const router = useRouter();

// 位置情報を取得する関数
const getLocation = async () => {
  if (navigator.geolocation) {
    loading.value = true;
    error.value = null;
    shrines.value = [];
    selectedShrine.value = null;

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        try {
          const response = await axios.get("/api/location", {
            params: { latitude, longitude },
          });
          if (response.data && response.data.shrines) {
            shrines.value = response.data.shrines.map((shrine) => ({
              name: shrine.name,
              address: shrine.address,
              distance: shrine.distance,
            }));
          } else {
            error.value = "データの取得に失敗しました。";
          }
        } catch (err) {
          error.value = "サーバーとの通信に失敗しました。";
        } finally {
          loading.value = false;
        }
      },
      () => {
        error.value = "位置情報の取得に失敗しました。";
        loading.value = false;
      }
    );
  } else {
    error.value = "位置情報が利用できません。";
  }
};

// 神社を選択する関数
const selectShrine = (shrine) => {
  selectedShrine.value = shrine;
};

// 特定のページへ遷移する関数
const navigateToGodcome = () => {
  if (selectedShrine.value) {
    router.push({ path: "./Godcome", query: { shrine: selectedShrine.value.name } });
  }
};

// コンポーネントがマウントされたときに位置情報を取得
onMounted(() => {
  getLocation();
});
</script>

<template>
  <div class="shrine-selection">
    <!-- 全体の背景画像 -->
    <div class="background-container">
      <img
        loading="lazy"
        src="@/assets/img/new_background.png"
        class="background-image"
        alt=""
      />
      <img
        loading="lazy"
        src="@/assets/img/background-shrine-alpha.png"
        class="overlay-image"
        alt=""
      />
    </div>
    <!-- ヘッダー部分 -->
    <div class="header-section">
      <img
        loading="lazy"
        src="@/assets/img/location-header.png"
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

.background-image,
.overlay-image {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
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

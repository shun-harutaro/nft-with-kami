<template>
  <div>
    <h1>近くの神社を検索</h1>
    <button @click="getLocation">現在地を取得して神社を検索</button>
    <div v-if="loading">ロード中...</div>
    <div v-if="error">{{ error }}</div>
    <div v-if="!loading && !error && shrines.length > 0">
      <h2>神社リスト:</h2>
      <ul>
        <li v-for="shrine in shrines" :key="shrine.name">
          <strong>{{ shrine.name }}</strong> - {{ shrine.address }}
          <button @click="selectShrine(shrine)">選択</button>
        </li>
      </ul>
    </div>
    <div v-if="selectedShrine">
      <h2>選択した神社:</h2>
      <p><strong>名前:</strong> {{ selectedShrine.name }}</p>
      <p><strong>住所:</strong> {{ selectedShrine.address }}</p>
    </div>
    <div v-if="!loading && !error && shrines.length === 0">神社が見つかりませんでした。</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      shrines: [], // 取得した神社のリスト
      selectedShrine: null, // 選択された神社
      loading: false, // ロード中フラグ
      error: null, // エラーメッセージ
    };
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
              const response = await fetch(
                `http://localhost:8000/location?latitude=${latitude}&longitude=${longitude}`
              );
              const data = await response.json();

              if (data.shrines) {
                this.shrines = data.shrines;
              } else {
                this.error = "データの取得に失敗しました。";
              }
            } catch (err) {
              this.error = "サーバーとの通信に失敗しました。";
            } finally {
              this.loading = false;
            }
          },
          (error) => {
            this.error = "位置情報の取得に失敗しました。";
            this.loading = false;
          }
        );
      } else {
        this.error = "位置情報が利用できません。";
      }
    },
    selectShrine(shrine) {
      // 選択された神社を更新
      this.selectedShrine = shrine;
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 1.5em;
  margin-bottom: 1em;
}

button {
  padding: 0.5em 1em;
  font-size: 1em;
  cursor: pointer;
  margin-left: 0.5em;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 0.5em 0;
}

strong {
  margin-right: 1em;
}
</style>

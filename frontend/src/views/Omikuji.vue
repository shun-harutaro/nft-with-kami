<template>
  <div class="result-screen">
    <div class="result-container">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/5e81f6d4ca789c8e3f9077e0b717f7c8b773568f91ec42fd69779d2e78a5813b?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
        class="background-image"
        alt=""
      />
      <div class="fortune-display">
        <img v-if="blobUrl" :src="blobUrl" alt="Generated Omikuji" />
        <div class="container">
          <div class="var-box">Token ID<br> <span id="var1"></span></div>
          <div class="var-box">Blockchain<br>Polygon</div>
          <div class="var-box">Token Standard<br>ERC-72 </div>
          <div class="var-box">Contract Address<br>0xfB40b73E6cEe109Ae7614e621ffA841Dd1EB1584</div>
          <div class="var-box">Transaction Hash<br> <span id="var2"></span></div>
        </div>
      </div>
      <div class="share-section">
        <button
          class="share-button"
          tabindex="0"
          @click="handleShare"
          aria-label="おみくじをシェア">
          <span>おみくじをシェア</span>
        </button>
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/1b3025bf1577dd0e3f2ae1f42ff1ae5f416bca32090785e1241417b7bc11443d?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
          class="share-icon"
          alt="Share fortune result"
        />
      </div>
      <button
         class="return-button"
         tabindex="0"
         @click="handleReturn"
         aria-label="最初へ戻る">
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/37658439fc1d41fe43bdb43b169f19d1626b20f05a953ebe1668ba8a62c7f442?placeholderIfAbsent=true&apiKey=d15c8345fe15403fbf2733b286d943d4"
          class="return-icon"
          alt=""
        />
        <span class="return-text">最初に戻る</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();

const picture = "https://tyoudoii-illust.com/wp-content/uploads/2024/07/oksign_businessman_simple-300x282.png";

const omikuziText = {
  "運勢": "大吉",
  "願望": "多くの思いを乗せ...",
  "健康": "日々の生活tinnpoを整えれば...",
  "金運": "自分のtinnpo強みを活かして...",
  "学問": "劇的にtinpo伸時期timm中して...",
  "恋愛": "信じ合うことtinnpotinnpo離に打ち勝て...",
  "神託": "一輝よ、朝の目覚めtinnpoせずに新たな環境で暮らすと..."
};

const blobUrl = ref(null);

onMounted(async () => {
  try {
    // おみくじ画像生成リクエスト
    const response = await axios.post(
      `/api/omikuzi?shrine_name=${encodeURIComponent('拳母神社')}&icon_url=${encodeURIComponent(picture)}`,
      omikuziText,
      {
        headers: {
          'Content-Type': 'application/json'
        },
        responseType: 'blob' // 画像をblobで受け取る
      }
    );
    // 生成された画像を表示
    blobUrl.value = URL.createObjectURL(response.data);

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
    document.getElementById("var1").textContent = metadataResponse.data.tokenId;
    document.getElementById("var2").textContent = metadataResponse.data.transactionHash;

    console.log("NFT Token ID:", metadataResponse.data.tokenId);
  } catch (error) {
    console.error("エラーが発生しました:", error);
  }
});

const handleShare = () => {
  // TODO: シェア機能実装
};

const handleReturn = () => {
  router.push("/");
};



</script>

<style scoped>
.result-screen {
  background-color: rgba(245, 239, 219, 1);
  display: flex;
  max-width: 480px;
  width: 100%;
  flex-direction: column;
  overflow: hidden;
  color: rgba(0, 0, 0, 1);
  font-weight: 400;
  text-align: center;
  margin: 0 auto;
}

.result-container {
  display: flex;
  flex-direction: column;
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
  padding: 174px 0 27px;
}

.background-image {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

.fortune-display {
  position: relative;
  display: flex;
  min-height: 395px;
  width: 100%;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  align-items: center; /* 中央寄せしたい場合 */
}

.fortune-display img {
  max-width: 100%;
  height: auto;
  object-fit: contain;
}

.share-section {
  position: relative;
  display: flex;
  gap: 11px;
  font-size: 40px;
}

.share-button {
  align-self: start;
  flex-grow: 1;
  flex-basis: auto;
  border: 1px solid rgba(0, 0, 0, 1);
  background: none;
  cursor: pointer;
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  font-size: 30px;
}

.share-icon {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 70px;
}

.return-button {
  display: flex;
  flex-direction: column;
  position: relative;
  border-radius: 30px;
  box-shadow: 4px 20px 4px rgba(0, 0, 0, 0.5);
  align-self: center;
  aspect-ratio: 1.777;
  margin-top: 20px;
  width: 100%;
  max-width: 295px;
  font-size: 48px;
  padding: 61px 33px;
  border: 1px solid rgba(0, 0, 0, 1);
  background: none;
  cursor: pointer;
  font-family: inherit;
  color: inherit;
}

.return-icon {
  width: 100%;
  height: 100%;
  object-fit: contain;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.return-text {
  position: relative;
  z-index: 2;
  font-size: inherit;
  color: inherit;
  font-size: 45px;
  text-align: center;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  max-width: 300px;
  margin-top: 20px;
  width: 90%;
  margin-left: auto;
  margin-right: auto;
  font-size: 18px;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.var-box {
  background: #fff; 
  border: 2px solid #333; 
  border-radius: 10px; 
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  line-height: 1.4;
  overflow-wrap: break-word;
  word-break: break-all;
  text-align: center; /* 全て中央揃えで統一 */
}

.var-box span {
  font-weight: bold;
  color: #000;
  display: block;
  margin-top: 5px;
}

/* Token ID・他のボックスとの統一感を確保するため特別なスタイルは控える */
/* もし全て同じならこのセレクタは不要 */

/* Transaction Hash を少し読みやすくするための微調整のみ */





</style>

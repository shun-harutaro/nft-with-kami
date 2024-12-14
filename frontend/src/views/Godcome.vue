<script>
import axios from 'axios';
import { useRouter } from 'vue-router'

const router = useRouter();

export default {
  data() {
    return {
      messages: [], // チャットメッセージ
      threadId: "", // スレッドID
      text: "", // GPTが生成した文章
    };
  },
  methods: {
    // shrine情報に基づくメッセージを取得
    async fetchMessages() {
      const shrineName = this.$route.query.shrine; // 正しい $route オブジェクトを使用
      if (!shrineName) {
        console.error("Shrine name is missing in the query.");
        return;
      }

      try {
        // shrine情報をAPIに送信してレスポンスを取得
        console.log(shrineName)
        const response = await axios.post(`/api/gpt/shrine-info?shrine=${shrineName}`, {
          headers: {
            "Content-Type": "text/plain",
          },
        });

        // APIのレスポンスからtextとthread_idを取得
        const { text, thread_id } = response.data;

        // メッセージとスレッドIDを設定
        this.messages.push({
          id: Date.now(),
          sender: "system",
          text: text,
        });
        this.threadId = thread_id;
        this.text = text;

        // メッセージが取得できたら次のページに遷移
        this.navigateToTalk();
      } catch (error) {
        console.error("Failed to fetch messages:", error);
      }
    },

    // Talkページに遷移
    navigateToTalk() {
      if (!this.threadId || !this.text) {
        console.error("Cannot navigate to talk page without threadId or text.");
        return;
      }
      this.$router.push({
        path: '/talk',
        query: {
          threadId: this.threadId,
          text: this.text, // textも次のページに渡す
        },
      });
    },
  },
  mounted() {
    this.fetchMessages(); // コンポーネントのマウント時にメッセージを取得
  },
};

const fetchShrine = () => {
  /* TODO 実装 */
};

// ページ表示後に5秒後の遷移を設定
setTimeout(() => {
  router.push('/talk'); // Talk.vue へのルートパスに遷移
}, 5000);
</script>

<template>
  <section class="hero-section" role="banner">
    <img
      loading="lazy"
      src="@/assets/img/god-background.png"
      class="hero-background"
      alt=""
    />
    <img
      loading="lazy"
      src="@/assets/img/god.png"
      class="hero-foreground"
      alt=""
    />
  </section>
</template>

<style scoped>
.hero-section {
  display: flex;
  flex-direction: column;
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
  padding: 311px 0 0;
}

.hero-background {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

.hero-foreground {
  aspect-ratio: 0.73;
  object-fit: contain;
  object-position: center;
  width: 100%;
  z-index: 10;

  /* フェードアニメーション */
  opacity: 0;
  animation: fadeIn 2s ease-in forwards;
}

/* アニメーション定義 */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>

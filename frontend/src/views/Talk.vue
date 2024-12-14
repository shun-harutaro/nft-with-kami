<template>
  <div class="chat-container">
    <div class="background-container">
      <img
        loading="lazy"
        src="@/assets/img/god-background.png"
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
    <div class="messages" ref="messageList">
      <div
        v-for="message in messages"
        :key="message.id"
        :class="['message', message.sender === 'me' ? 'sent' : 'received']"
      >
        <!-- 神様側のアイコンと背景 -->
        <div class="icon-wrapper" v-if="message.sender !== 'me'">
          <div class="icon-background"></div>
          <img
            src="@/assets/img/god-icon.png" 
            alt="神様アイコン"
            class="icon-image"
          />
        </div>
        <!-- ユーザー側のアイコン -->
        <div class="icon" v-if="message.sender === 'me'">
          <img
            :src="profileImageUrl" 
            alt="ユーザーアイコン"
          />
        </div>
        <div class="bubble">{{ message.text }}</div>
      </div>
    </div>
    <div class="input-area">
      <input v-model="newMessage" placeholder="メッセージを入力" />
      <button @click="sendMessage" class="send-button"></button>
    </div>
  </div>
</template>

<script>
import { computed, ref, nextTick } from "vue";
import { useUserProfileStore } from "@/stores/userProfileStore";
import axios from "axios";

export default {
  setup() {
    const userProfileStore = useUserProfileStore();
    const profileImageUrl = computed(() => userProfileStore.profileImageUrl);
    return {
      profileImageUrl,
    };
  },
  data() {
    return {
      messages: [], // チャットメッセージ
      newMessage: "", // 入力中のメッセージ
      threadId: "", // スレッドID
    };
  },
  methods: {
    // メッセージ送信
    async sendMessage() {
      if (this.newMessage.trim() === "") return; // 空メッセージは無視

      const message = {
        id: Date.now(),
        sender: "me",
        text: this.newMessage,
      };

      // 入力メッセージを画面に即座に反映
      this.messages.push(message);
      this.scrollToEnd();

      const userMessage = this.newMessage; // 送信前に値を保持
      this.newMessage = ""; // 入力欄をクリア

      try {
        console.log("Thread ID:", this.threadId);

        // サーバーにメッセージを送信
        const response = await axios.post(`/api/gpt/talking?text=${userMessage}&thread_id=${this.threadId}`);

        const { text, thread_id, end_point } = response.data;

        // サーバーからの応答をチャットメッセージに追加
        this.messages.push({
          id: Date.now(),
          sender: "system",
          text: text,
        });

        this.scrollToEnd(); // 応答追加後にスクロール

        // スレッドIDを更新
        this.threadId = thread_id;

        // end_point が 1 の場合、/loading ページに遷移
        if (end_point === 1) {
          console.log("Waiting for 5 seconds before navigation...");
          await new Promise((resolve) => setTimeout(resolve, 5000));
          console.log("Navigating to /loading");
          this.$router.push({
            path: "/loading",
            query: {
              threadId: thread_id,
            },
          });
        }
      } catch (error) {
        console.error("Failed to send message:", error);

        // エラー時のメッセージを画面に表示
        this.messages.push({
          id: Date.now(),
          sender: "system",
          text: "メッセージの送信に失敗しました。",
        });

        this.scrollToEnd(); // エラーメッセージ追加後にスクロール
      }
    },
    // メッセージリストの一番下にスクロール
    scrollToEnd() {
      nextTick(() => {
        const messageList = this.$refs.messageList;
        if (messageList) {
          messageList.scrollTop = messageList.scrollHeight;
        }
      });
    },
  },
  mounted() {
    const { threadId, text } = this.$route.query;

    if (!threadId || !text) {
      console.error("Missing threadId or text in query parameters.");
      return;
    }

    this.messages.push({
      id: Date.now(),
      sender: "system",
      text: text,
    });

    this.threadId = threadId;
    this.scrollToEnd(); // 初期メッセージ表示時にスクロール
  },
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 600px;
  margin: 0 auto;
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

.messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  z-index: 10;
  position: relative;
}

.message {
  display: flex;
  align-items: flex-start;
  margin-bottom: 10px;
}
.message.sent {
  flex-direction: row-reverse;
}
.message.received {
  flex-direction: row;
}

/* 神様側アイコンの背景 */
.icon-wrapper {
  position: relative;
  width: 50px;
  height: 50px;
  margin-right: 10px;
}
.icon-background {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: #ffe0b2;
  border-radius: 50%;
  z-index: -1;
}
.icon-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

/* ユーザー側アイコン */
.icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  margin-left: 10px;
}
.icon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 吹き出し */
.bubble {
  position: relative;
  z-index: 10;
  max-width: 70%;
  padding: 10px;
  border-radius: 15px;
  background-color: #dcf8c6;
  word-wrap: break-word;
  color: #000000;
}
.message.received .bubble {
  background-color: #fff;
  border: 1px solid #ddd;
}

/* 入力エリア */
.input-area {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
  background-color: #fff;
}

/* テキストボックス */
input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

/* 送信ボタン（三角形） */
.send-button {
  position: relative;
  width: 36px;
  height: 36px;
  margin-left: 10px;
  background-color: #007bff;
  border: none;
  clip-path: polygon(100% 50%, 0 0, 0 100%);
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.send-button::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 0;
  right: 50%; /* 中央まで */
  height: 2px; /* 線の太さ */
  background-color: #ffffff;
  transform: translateY(-50%);
}

.send-button:hover {
  background-color: #0056b3;
}


</style>

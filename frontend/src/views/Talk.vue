<template>
  <div class="chat-container">
    <div class="messages">
      <div
        v-for="message in messages"
        :key="message.id"
        :class="['message', message.sender === 'me' ? 'sent' : 'received']"
      >
        <div class="bubble">{{ message.text }}</div>
      </div>
    </div>
    <button>デバッグ</button>
    <div class="input-area">
      <input v-model="newMessage" placeholder="メッセージを入力" />
      <button @click="sendMessage">送信</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      messages: [], // チャットメッセージ
      newMessage: "", // 入力中のメッセージ
      threadId: "", // スレッドID（必要に応じて初期化）
    };
  },
  methods: {
    // メッセージの初期取得
    async fetchMessages() {
      try {
        const response = await axios.post("/api/gpt/shrine-info?shrine=拳母神社",{
        headers: {
          "Content-Type": "text/plain", // リクエストの Content-Type を指定
        },
        });
        const { text, thread_id } = response.data;

        // 初期データを設定
        this.messages.push({
          id: Date.now(),
          sender: "system",
          text: text,
        });
        this.threadId = thread_id; // スレッドIDを保持
      } catch (error) {
        console.error("Failed to fetch messages:", error);
      }
    },

    // メッセージ送信
    async sendMessage() {
      if (this.newMessage.trim() === "") return;

      const message = {
        id: Date.now(),
        sender: "me",
        text: this.newMessage,
      };

      // 画面に即座に反映
      this.messages.push(message);
      const userMessage = this.newMessage;
      this.newMessage = "";

      try {
        console.log(this.threadId);
        // サーバーにメッセージを送信
        const response = await axios.post(`/api/gpt/talking?text=${userMessage}&thread_id=${this.threadId}`);

        const { text } = response.data;

        // サーバーからの応答を追加
        this.messages.push({
          id: Date.now(),
          sender: "system",
          text: text,
        });
      } catch (error) {
        console.error("Failed to send message:", error);

        // エラー表示用のメッセージを追加
        this.messages.push({
          id: Date.now(),
          sender: "system",
          text: "メッセージの送信に失敗しました。",
        });
      }
    },
  },
  mounted() {
    this.fetchMessages();
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
  border: 1px solid #ccc;
  background-color: #f7f7f7;
}
.messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}
.message {
  display: flex;
  margin-bottom: 10px;
}
.message.sent {
  justify-content: flex-end;
}
.message.received {
  justify-content: flex-start;
}
.bubble {
  max-width: 70%;
  padding: 10px;
  border-radius: 15px;
  background-color: #dcf8c6;
  word-wrap: break-word;
}
.message.received .bubble {
  background-color: #fff;
  border: 1px solid #ddd;
}
.input-area {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
  background-color: #fff;
}
input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
button {
  padding: 10px 15px;
  margin-left: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>

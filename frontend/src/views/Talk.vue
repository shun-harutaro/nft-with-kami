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
    <div class="input-area">
      <input v-model="newMessage" placeholder="メッセージを入力" />
      <button @click="sendMessage">送信</button>
    </div>
  </div>
</template>

<script>


import axios from 'axios';

export default {
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

        // スレッドIDを更新
        this.threadId = thread_id;
        console.log(end_point)
        // end_point が 1 の場合、/loading ページに遷移
        if (end_point === 1) {
          // 5秒待機処理
          console.log("Waiting for 5 seconds before navigation...");
          await new Promise((resolve) => setTimeout(resolve, 5000));
          
          console.log("Navigating to /loading");
          // 遷移処理
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
      }
    },
  },
  mounted() {
    // クエリパラメータから `text` と `threadId` を取得
    const { threadId, text } = this.$route.query;

    if (!threadId || !text) {
      console.error("Missing threadId or text in query parameters.");
      return;
    }

    // 初期メッセージを追加
    this.messages.push({
      id: Date.now(),
      sender: "system",
      text: text,
    });

    // スレッドIDを設定
    this.threadId = threadId;
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

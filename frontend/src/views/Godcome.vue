<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

// Reactive state
const messages = ref([]);
const threadId = ref('');
const text = ref('');

// Router & Route instances
const router = useRouter();
const route = useRoute();

// メッセージを取得
const fetchMessages = async () => {
  const shrineName = route.query.shrine;
  if (!shrineName) {
    console.error("Shrine name is missing in the query.");
    return;
  }

  try {
    console.log(shrineName);
    const response = await axios.post(`/api/gpt/shrine-info?shrine=${shrineName}`, {
      headers: {
        "Content-Type": "text/plain",
      },
    });

    const { text: responseText, thread_id } = response.data;

    // メッセージとスレッドIDを設定
    messages.value.push({
      id: Date.now(),
      sender: "system",
      text: responseText,
    });
    threadId.value = thread_id;
    text.value = responseText;

    // 次のページに遷移
    navigateToTalk();
  } catch (error) {
    console.error("Failed to fetch messages:", error);
  }
};

// Talkページに遷移
const navigateToTalk = () => {
  if (!threadId.value || !text.value) {
    console.error("Cannot navigate to talk page without threadId or text.");
    return;
  }

  router.push({
    path: '/talk',
    query: {
      threadId: threadId.value,
      text: text.value,
    },
  });
};

// コンポーネントのマウント時にメッセージを取得
onMounted(() => {
  fetchMessages();

  // 5秒後にTalkページへ遷移
  setTimeout(() => {
    router.push('/talk');
  }, 5000);
});
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

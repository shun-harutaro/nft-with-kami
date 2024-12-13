import { createRouter, createWebHistory } from "vue-router"
import { useUserProfileStore } from "@/stores/userProfileStore";

import Login from "./views/Login.vue"
import Location from "./views/Location.vue"
import Godcome from "./views/Godcome.vue"
import Omikuji from "./views/Omikuji.vue"
import Loading from "./views/Loading.vue"
import Talk from "./views/Talk.vue"

const routes = [
  { path: "/", name: "Login", component: Login },
  { path: "/location", component: Location },
  { path: "/godcome", component: Godcome },
  { path: "/omikuji", component: Omikuji},
  { path: "/loading", component: Loading},
  { path: "/talk", component: Talk},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// グローバルナビゲーションガードを追加
router.beforeEach(async (to, from, next) => {
  const store = useUserProfileStore();

  // ユーザーデータが未取得の場合、サーバーからフェッチ
  if (!store.isLoggedIn) {
    await store.fetchUserProfile();
  }

  // 認証が必要なルートの保護
  if (to.name !== "Login" && !store.isLoggedIn) {
    next({ name: "Login" }); // ログインしていない場合はホームにリダイレクト
  } else {
    next(); // 通常通りルートへ遷移
  }
});

export default router

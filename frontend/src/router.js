import { createRouter, createWebHistory } from "vue-router"

import Login from "./views/Login.vue"
import Callback from "./views/Callback.vue"

const routes = [
  { path: "/", component: Login },
  { path: "/callback", component: Callback }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

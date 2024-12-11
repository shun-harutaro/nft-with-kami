import { createRouter, createWebHistory } from "vue-router"

import Login from "./views/Login.vue"
import Location from "./views/Location.vue"
import Omikuji from "./views/Omikuji.vue"

const routes = [
  { path: "/", component: Login },
  { path: "/location", component: Location },
  { path: "/omikuji", component: Omikuji },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

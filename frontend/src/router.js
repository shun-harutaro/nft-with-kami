import { createRouter, createWebHistory } from "vue-router"

import Login from "./views/Login.vue"
import Location from "./views/Location.vue"
import Godcome from "./views/Godcome.vue"
import Omikuji from "./views/Omikuji.vue"

const routes = [
  { path: "/", component: Login },
  { path: "/location", component: Location },
  { path: "/godcome", component: Godcome },
  { path: "/omikuji", component: Omikuji},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

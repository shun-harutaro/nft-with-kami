import { createRouter, createWebHistory } from "vue-router"

import Login from "./views/Login.vue"
import Callback from "./views/Callback.vue"
import Location from "./views/Location.vue"
import Home from "./views/home.vue"

const routes = [
  { path: "/", component: Home },
  { path: "/callback", component: Callback },
  { path: "/location", component: Location }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

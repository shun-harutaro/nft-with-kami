import { createRouter, createWebHistory } from "vue-router"

import Login from "./views/Login.vue"
import Location from "./views/Location.vue"
import User from "./views/User.vue"

const routes = [
  { path: "/", component: Login },
  { path: "/location", component: Location },
  { path: "/user", component: User },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

import { createWebHistory, createRouter } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/DashBoard.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/accounts/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/accounts/Register.vue')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;

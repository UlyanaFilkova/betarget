import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import RegistrationView from "@/views/RegistrationView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/registration",
      name: "registration",
      component: RegistrationView,
    },
  ],
});

export default router;

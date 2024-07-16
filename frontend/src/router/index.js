import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import RegistrationView from "@/views/RegistrationView.vue";
import CrmView from "@/views/CrmView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/crm",
      name: "crm",
      component: CrmView,
    },
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

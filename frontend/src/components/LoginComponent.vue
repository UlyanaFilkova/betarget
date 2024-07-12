<script setup>
import "@/assets/css/login.css";
import { reactive, ref, onMounted, computed } from "vue";
import router from "@/router";
import { RouterLink } from "vue-router";
import axios from "axios";

const form = reactive({
  email: "",
  password: "",
});

const loginEmail = ref(null);
const loginPassword = ref(null);

const errors = reactive({
  email: "",
});

function validatePassword(password) {
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
  return passwordRegex.test(password);
}

onMounted(() => {
  loginEmail.value.addEventListener("focusout", (event) => {
    if (loginEmail.value.validity.typeMismatch) {
      errors.email = "Введите корректный email";
      loginEmail.value.addEventListener("input", (event) => {
        if (loginEmail.value.validity.typeMismatch) {
          errors.email = "Введите корректный email";
        } else {
          errors.email = "";
        }
      });
    } else {
      errors.email = "";
    }
  });

  loginPassword.value.addEventListener("focusout", (event) => {
    if (!validatePassword(loginPassword.value.value)) {
      errors.password =
        "Пароль должен быть не менее 8 символов и содержать большие буквы и цифры";
      loginPassword.value.addEventListener("input", (event) => {
        if (!validatePassword(loginPassword.value.value)) {
          errors.password =
            "Пароль должен быть не менее 8 символов и содержать большие буквы и цифры";
        } else {
          errors.password = "";
        }
      });
    } else {
      errors.password = "";
    }
  });
});

const handleSubmit = async () => {
  // если поля пусты или невалидны
  if (
    errors.email !== "" ||
    errors.password !== "" ||
    loginPassword.value.value === "" ||
    loginEmail === ""
  ) {
    return; 
  }
  const userData = {
    email: form.email,
    password: form.password,
  };

  try {
    console.log(userData);
    // const response = await axios.post("/api/jobs/", userData);
    // router.push(`/jobs/${response.data.id}`);
  } catch (error) {
    console.error("Error login", error);
  }
};
</script>

<template>
  <section class="login">
    <div class="login__wrapper">
      <h1 class="login__logo">Betarget</h1>
      <form novalidate class="login__form" @submit.prevent="handleSubmit">
        <input
          class="login__input"
          type="email"
          id="login__email"
          name="login__email"
          v-model="form.email"
          placeholder="Электронная почта"
          autocomplete="email"
          ref="loginEmail"
          required
        />
        <span
          :style="{ visibility: errors.email ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.email }}</span
        >
        <input
          class="login__input"
          type="password"
          id="login__password"
          name="login__password"
          v-model="form.password"
          placeholder="Пароль"
          autocomplete="current-password"
          ref="loginPassword"
          required
        />
        <span
          :style="{ visibility: errors.password ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.password }}</span
        >
        <button class="login__button" type="submit">Вход</button>
      </form>
      <div class="login__links">
        <RouterLink to="" class="login__link">Забыли пароль?</RouterLink>
        <RouterLink to="" class="login__link">Создать аккаунт</RouterLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import "@/assets/css/login.css";
import { reactive, ref, onMounted, computed } from "vue";
import router from "@/router";
import { RouterLink } from "vue-router";
import axios from "axios";
import qs from "qs";

const form = reactive({
  email: "",
  username: "",
  password: "",
  repeatPassword: "",
});

const loginEmail = ref(null);
const loginUsername = ref(null);
const loginPassword = ref(null);
const loginRepeatPassword = ref(null);

const errors = reactive({
  email: "",
  username: "",
  password: "",
  repeatPassword: "",
  emptyFields: "",
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
        "Пароль должен содержать не менее 8 символов и включать большие буквы и цифры";
      loginPassword.value.addEventListener("input", (event) => {
        if (!validatePassword(loginPassword.value.value)) {
          errors.password =
            "Пароль должен содержать не менее 8 символов и включать большие буквы и цифры";
        } else {
          errors.password = "";
        }
      });
    } else {
      errors.password = "";
    }
  });

  loginRepeatPassword.value.addEventListener("focusout", (event) => {
    if (loginRepeatPassword.value.value !== loginPassword.value.value) {
      errors.repeatPassword = "Пароли не совпадают";
      loginRepeatPassword.value.addEventListener("input", (event) => {
        if (!validatePassword(loginPassword.value.value)) {
          errors.repeatPassword = "Пароли не совпадают";
        } else {
          errors.repeatPassword = "";
        }
      });
    } else {
      errors.repeatPassword = "";
    }
  });
});

const handleSubmit = async () => {
  // если поля пусты или невалидны
  if (
    loginRepeatPassword.value.value === "" ||
    loginUsername.value.value === "" ||
    loginPassword.value.value === "" ||
    loginEmail.value.value === ""
  ) {
    errors.emptyFields = "Заполните, пожалуйста, все поля";
  } else {
    errors.emptyFields = "";
  }
  if (
    errors.repeatPassword !== "" ||
    errors.username !== "" ||
    errors.email !== "" ||
    errors.password !== "" ||
    errors.emptyFields
  ) {
    return;
  }
  const userData = {
    username: form.username,
    email: form.email,
    password: form.password,
    is_active: true,
    is_superuser: false,
    is_verified: false,
    telegram: null,
    whatsapp: null,
    linkedin: null,
    github: null,
    phone_number: null,
    profile_picture: null,
  };

  try {
    console.log(userData);
    const response = await axios.post("/api/register", userData, {
      headers: { "Content-Type": "application/json" },
    });
    console.log(response.data);
  } catch (error) {
    console.error("Error register", error);
  }
};
</script>

<template>
  <section class="login">
    <div class="login__wrapper">
      <h1 class="login__logo">Betarget</h1>
      <form novalidate class="login__form" @submit.prevent="handleSubmit">
        <span
          :style="{ visibility: errors.emptyFields ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.emptyFields }}</span
        >
        <input
          class="login__input"
          type="username"
          id="login__username"
          name="login__username"
          v-model="form.username"
          placeholder="Имя пользователя"
          autocomplete="username"
          ref="loginUsername"
          required
        />
        <span
          :style="{ visibility: errors.username ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.username }}</span
        >
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
          autocomplete="new-password"
          ref="loginPassword"
          required
        />
        <span
          :style="{ visibility: errors.password ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.password }}</span
        >
        <input
          class="login__input"
          type="password"
          id="login__repeat_password"
          name="login__repeat_password"
          v-model="form.repeatPassword"
          placeholder="Повторите пароль"
          autocomplete="new-password"
          ref="loginRepeatPassword"
          required
        />
        <span
          :style="{ visibility: errors.repeatPassword ? 'visible' : 'hidden' }"
          class="login__error"
          >{{ errors.repeatPassword }}</span
        >
        <button class="login__button" type="submit">Регистрация</button>
      </form>
      <div class="login__links">
        <RouterLink to="/login" class="login__link"
          >Уже есть аккаунт? Войти</RouterLink
        >
      </div>
    </div>
  </section>
</template>

<style scoped>
.login__links {
  justify-content: center;
}
</style>
